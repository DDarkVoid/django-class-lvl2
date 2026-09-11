"""Views for students app."""

from rest_framework import viewsets

from apps.students.models import Group, Student
from apps.students.serializers import GroupSerializer, StudentSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """CRUD for Group model."""

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """CRUD for Student model."""

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
