from rest_framework.routers import DefaultRouter

from schedule.views import ScheduleViewSet

router = DefaultRouter()
router.register("", ScheduleViewSet, basename="schedule")

urlpatterns = router.urls
app_name = "schedule"
