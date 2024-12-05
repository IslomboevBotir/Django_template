from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('employee', 'Сотрудник'),
        ('manager', 'Начальник'),
        ('assistant', 'Помощник начальника'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')
