"""Models for students app."""

from django.db import models

GROUP_NAME_MAX_LENGTH = 100
STUDENT_NAME_MAX_LENGTH = 200
STUDENT_ID_MAX_LENGTH = 20


class Group(models.Model):
    """Student group."""

    name = models.CharField(max_length=GROUP_NAME_MAX_LENGTH)
    monitor = models.ForeignKey(
        'Student',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='monitored_group',
    )

    def __str__(self) -> str:
        """Return group name."""
        return self.name


class Student(models.Model):
    """Student."""

    full_name = models.CharField(max_length=STUDENT_NAME_MAX_LENGTH)
    birth_date = models.DateField()
    student_id = models.CharField(
        max_length=STUDENT_ID_MAX_LENGTH,
        unique=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        related_name='students',
    )

    def __str__(self) -> str:
        """Return student full name."""
        return self.full_name
