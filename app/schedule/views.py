from django.db.models import Count
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from schedule.filters import ScheduleClassNameFilter, ScheduleForTodayFilter
from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer


class ScheduleViewSet(ListModelMixin, GenericViewSet):
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (ScheduleForTodayFilter, ScheduleClassNameFilter)

    def get_queryset(self):
        return Schedule.objects.select_related(
            "related_class",
            "subject",
            "subject__teacher",
        ).annotate(
            class_student_count=Count("related_class__students"),
        )
