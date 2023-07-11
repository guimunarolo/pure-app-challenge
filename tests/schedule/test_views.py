import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestScheduleViewSet:
    def test_list_ok(
        self, client, schedule, teacher, school_class, subject, student
    ):
        response = client.get(reverse("schedule-list"))

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == [
            {
                "day_of_week": schedule.day_of_week,
                "hour": schedule.hour,
                "subject": {"name": subject.name},
                "teacher": {"name": teacher.name},
                "class": {
                    "name": school_class.name,
                    "student_count": school_class.student_count,
                },
            }
        ]
