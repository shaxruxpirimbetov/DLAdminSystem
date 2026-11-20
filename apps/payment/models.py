from django.db import models
from apps.student.models import Student
from apps.group.models import Group

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="payment_student")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="payment_group")
    amount = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.student)

    class Meta:
        verbose_name_plural = "Payment"
        ordering = ["-created_at"]