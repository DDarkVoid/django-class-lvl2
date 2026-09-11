"""URLs for students app."""

from rest_framework.routers import DefaultRouter

from apps.students.views import GroupViewSet, StudentViewSet

router = DefaultRouter()
router.register('groups', GroupViewSet)
router.register('students', StudentViewSet)

urlpatterns = router.urls
