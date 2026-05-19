import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from todos.models import Todo

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='password123')

@pytest.fixture
def user2(db):
    return User.objects.create_user(username='testuser2', password='password123')

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client

@pytest.fixture
def sample_todo(user):
    return Todo.objects.create(title="Sample Todo", owner=user)