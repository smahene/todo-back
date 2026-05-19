from rest_framework import viewsets, permissions
from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

def health_check(request):
    return JsonResponse({"status": "ok"})

def trigger_error(request):
    division_by_zero = 1 / 0