
from django.urls import path
from todos import views

urlpatterns = [
    path('todolist/', views.TodolistView.as_view(), name='todolist_view'),
]
