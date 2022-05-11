from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.utils import BaseModel


class User(BaseModel, AbstractUser):
    class USERTYPES(models.TextChoices):
        STUDENT = "ST", "Student"
        LECTURER = "LC", "Lecturer"

    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    username = models.CharField(max_length=100, unique=True)
    usertype = models.CharField(
        max_length=15, default=USERTYPES.STUDENT, choices=USERTYPES.choices
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
