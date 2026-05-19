import pytest
from django.core.exceptions import ValidationError
from todos.models import Todo

pytestmark = pytest.mark.django_db

def test_todo_creation(user):
    todo = Todo.objects.create(title="Test Todo", owner=user)
    assert todo.title == "Test Todo"
    assert todo.completed == False
    assert todo.owner == user
    assert str(todo) == "Test Todo"

def test_todo_requires_title(user):
    todo = Todo(title="", owner=user)
    with pytest.raises(ValidationError):
        todo.full_clean()

def test_mark_as_complete(sample_todo):
    assert sample_todo.completed == False
    sample_todo.mark_as_complete()
    sample_todo.refresh_from_db()
    assert sample_todo.completed == True