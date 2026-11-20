from django.db import models
from apps.student.models import Student

class Group(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, blank=True, related_name="group_students")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Groups"
        ordering = ["-created_at"]