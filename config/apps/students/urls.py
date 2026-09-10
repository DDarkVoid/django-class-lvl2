"""URLs for students app."""

from apps.students.views import GroupViewSet, StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('groups', GroupViewSet)
router.register('students', StudentViewSet)

urlpatterns = router.urls
