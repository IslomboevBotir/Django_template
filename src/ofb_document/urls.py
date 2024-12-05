from django.urls import path
from .views import (
    DocumentsViews,
    DocumentUploadViews,
    DocumentDetailViews,
    DocumentStatusUpdateViews,
    AssignDocumentViews
)

urlpatterns = [
    path("", DocumentsViews.as_view()),
    path("upload", DocumentUploadViews.as_view()),
    path("<int:pk>", DocumentDetailViews.as_view()),
    path("status/<int:pk>", DocumentStatusUpdateViews.as_view()),
    path("assign/<int:pk>", AssignDocumentViews.as_view()),
]
