"""Admin for students app."""

from apps.students.models import Group, Student
from django.contrib import admin

admin.site.register(Group)
admin.site.register(Student)
