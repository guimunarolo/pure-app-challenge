from datetime import date

from rest_framework import filters


class ScheduleForTodayFilter(filters.BaseFilterBackend):
    """Filter Schedule for today."""

    def filter_queryset(self, request, queryset, view):
        for_today = request.query_params.get("for_today")
        if for_today and for_today.lower() == "true":
            return queryset.filter(day_of_week=date.today().isoweekday())

        return queryset
