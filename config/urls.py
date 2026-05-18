from django.contrib import admin
from django.urls import path, include
from todos.views import health_check
from todos.views import health_check, trigger_error

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todos.urls')),
    path('health/', health_check),
    path('error/', trigger_error),
]