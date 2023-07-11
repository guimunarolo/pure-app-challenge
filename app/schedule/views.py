from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import GenericViewSet

from schedule.filters import ScheduleForTodayFilter
from schedule.models import Schedule
from schedule.serializers import ScheduleSerializer


class ScheduleViewSet(ListModelMixin, GenericViewSet):
    queryset = Schedule.objects.select_related(
        "related_class", "subject", "subject__teacher"
    )
    serializer_class = ScheduleSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (ScheduleForTodayFilter,)
