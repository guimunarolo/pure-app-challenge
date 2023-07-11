from django.urls import include, path

urlpatterns = [
    path("schedule/", include("schedule.urls", namespace="schedule")),
]
