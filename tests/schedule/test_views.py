from datetime import date

import pytest
from django.urls import reverse
from rest_framework import status

from tests.schedule.factories import ScheduleFactory

pytestmark = pytest.mark.django_db


class TestScheduleViewSet:
    def test_list_ok(self, client, schedule, teacher, school_class, subject):
        response = client.get(reverse("schedule:schedule-list"))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            {
                "day_of_week": schedule.day_of_week,
                "hour": schedule.hour,
                "subject": {"name": subject.name},
                "teacher": {"name": teacher.name},
                "class": {
                    "name": school_class.name,
                    "student_count": school_class.students.count(),
                },
            }
        ]

    def test_list_for_today_filter(self, client):
        today_week_day = date.today().isoweekday()
        # today's schedule
        ScheduleFactory(day_of_week=today_week_day)
        # tomorrow's schedule
        ScheduleFactory(
            day_of_week=today_week_day + 1 if today_week_day < 7 else 1
        )

        response = client.get(
            reverse("schedule:schedule-list"), {"for_today": "true"}
        )
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert len(response_data) == 1
        assert response_data[0]["day_of_week"] == today_week_day

    def test_list_class_name_filter(self, client):
        class_name = "5A"
        # listed schedule
        ScheduleFactory(related_class__name=class_name)
        # unlisted schedule
        ScheduleFactory(related_class__name="some class")

        response = client.get(
            reverse("schedule:schedule-list"), {"class_name": class_name}
        )
        response_data = response.json()

        assert response.status_code == status.HTTP_200_OK
        assert len(response_data) == 1
        assert response_data[0]["class"]["name"] == class_name
