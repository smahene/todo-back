import pytest
from rest_framework import status
from todos.models import Todo

pytestmark = pytest.mark.django_db

def test_get_todos_unauthenticated(api_client):
    response = api_client.get('/api/todos/')
    assert response.status_code in [status.HTTP_401_UNAUTHORIZED, status.HTTP_403_FORBIDDEN]

def test_create_todo(authenticated_client, user):
    response = authenticated_client.post('/api/todos/', {'title': 'New Todo'}, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Todo.objects.count() == 1

def test_create_todo_empty_title(authenticated_client):
    response = authenticated_client.post('/api/todos/', {'title': ''}, format='json')
    assert response.status_code == status.HTTP_400_BAD_REQUEST

def test_list_todos(authenticated_client, sample_todo, user2):
    Todo.objects.create(title="Other user todo", owner=user2)
    response = authenticated_client.get('/api/todos/')
    assert response.status_code == status.HTTP_200_OK

def test_delete_todo(authenticated_client, sample_todo):
    response = authenticated_client.delete(f'/api/todos/{sample_todo.id}/')
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Todo.objects.count() == 0

def test_user_cannot_delete_other_user_todo(authenticated_client, user2):
    other_todo = Todo.objects.create(title="Other todo", owner=user2)
    response = authenticated_client.delete(f'/api/todos/{other_todo.id}/')
    assert response.status_code == status.HTTP_404_NOT_FOUND