from django.db import models
from django.contrib.auth.models import AbstractUser

from .constants import ROLE_CHOICES


class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='employee'
    )
