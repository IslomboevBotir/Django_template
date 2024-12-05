from django.urls import path
from .views import RegistrationUserViews

urlpatterns = [
    path('/register', RegistrationUserViews.as_view()),
]
