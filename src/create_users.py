import os
import django

from django.contrib.auth import get_user_model


def create_users():
    User = get_user_model()
    User.objects.create_user(
        username='user1',
        password='user1user1',
        email='user1@example.com',
        role='employee',
        is_staff=True
    )
    User.objects.create_user(
        username='user3',
        password='user3user3',
        email='user3@example.com',
        role='assistant',
        is_staff=True
    )
    User.objects.create_user(
        username='user2',
        password='user2user2',
        email='user2@example.com',
        role='manager',
        is_staff=True
    )


if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.ofb_api.settings')
    django.setup()
    create_users()
