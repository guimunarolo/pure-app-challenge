from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from common.models import UUIDModel
from schedule.constants import DAY_CHOICES


class Class(UUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    @property
    def student_count(self):
        return self.students.count()


class Student(UUIDModel):
    name = models.CharField(max_length=255)
    classes = models.ManyToManyField("Class", related_name="students")

    def __str__(self):
        return self.name


class Teacher(UUIDModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Subject(UUIDModel):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(
        "Teacher", related_name="subjects", on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class Schedule(UUIDModel):
    related_class = models.ForeignKey(
        "Class", related_name="schedule", on_delete=models.PROTECT
    )
    subject = models.ForeignKey(
        "Subject", related_name="schedule", on_delete=models.PROTECT
    )
    day_of_week = models.IntegerField(
        choices=DAY_CHOICES, help_text="Monday = 1 - Sunday = 7"
    )
    hour = models.IntegerField(
        validators=(MinValueValidator(0), MaxValueValidator(23)),
        help_text="Format: 24 hours",
    )

    class Meta:
        ordering = ("day_of_week", "hour")

    def __str__(self):
        return self.uuid
