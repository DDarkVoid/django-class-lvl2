"""URLs for students app."""

from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.students.views import GroupViewSet, StudentViewSet, TokenUsageView

router = DefaultRouter()
router.register('groups', GroupViewSet)
router.register('students', StudentViewSet)

urlpatterns = [
    path('token-usage/', TokenUsageView.as_view(), name='token_usage'),
    *router.urls,
]
