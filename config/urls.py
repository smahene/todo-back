from django.contrib import admin
from django.urls import path, include
from todos.views import health_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    path('health/', health_check),
]