from rest_framework import viewsets
from django.http import JsonResponse
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('-created_at')
    serializer_class = TodoSerializer

def health_check(request):
    return JsonResponse({"status": "ok"})