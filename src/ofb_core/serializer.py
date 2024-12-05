from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import CustomUser
from .constants import ROLE_CHOICES


class RegistrationSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=ROLE_CHOICES, default='employee')
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'role']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)
