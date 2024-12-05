from django.urls import path
from .views import (
    DocumentsViews,
    DocumentUploadViews,
    DocumentDetailView,
    DocumentStatusUpdateView,
    AssignDocumentView
)

urlpatterns = [
    path("", DocumentsViews.as_view()),
    path("upload", DocumentUploadViews.as_view()),
    path("<int:pk>", DocumentDetailView.as_view()),
    path("status/<int:pk>", DocumentStatusUpdateView.as_view()),
    path("assign/<int:pk>", AssignDocumentView.as_view()),
]
