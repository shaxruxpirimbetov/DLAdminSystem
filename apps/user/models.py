from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        SUPERADMIN = "SUPERADMIN"
        MENTOR = "MENTOR"

    role = models.CharField(
        max_length=20,
        choices=Role
    )
    platform_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return f"User {self.username}"

    class Meta:
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]