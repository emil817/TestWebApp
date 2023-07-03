from django.contrib import admin
from django.urls import path, include
from .views import get_movies, get_diagram
urlpatterns = [
    path('', get_movies),
    path('diagram/', get_diagram)
]