"""Serializers for students app."""

from apps.students.models import Group, Student
from rest_framework import serializers


class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model."""

    class Meta(object):
        """Serializer metadata."""

        model = Student
        fields = ('id', 'full_name', 'birth_date', 'student_id', 'group')


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model."""

    class Meta(object):
        """Serializer metadata."""

        model = Group
        fields = ('id', 'name', 'monitor')
