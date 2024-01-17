# QuizMestreQ/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("usuarios/", include('usuarios.urls')),  # Use "usuarios/" ao invés de "ususarios/"
]
