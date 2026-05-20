from rest_framework import viewsets
from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save()

def health_check(request):
    return JsonResponse({"status": "ok"})

def trigger_error(request):
    division_by_zero = 1 / 0