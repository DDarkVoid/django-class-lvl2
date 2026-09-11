"""Admin for students app."""

from django.contrib import admin

from apps.students.models import Group, Student

admin.site.register(Group)
admin.site.register(Student)
