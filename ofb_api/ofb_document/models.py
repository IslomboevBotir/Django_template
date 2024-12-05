from django.db import models
from django.conf import settings

from .constants import TYPE_CHOICES, STATUS_CHOICES


class Documents(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='documents/')
    mfo = models.CharField(max_length=20)
    document_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )
    message = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='created_documents'
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_documents'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
