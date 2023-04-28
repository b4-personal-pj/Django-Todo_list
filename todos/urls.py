
from django.urls import path
from todos import views

urlpatterns = [
    path('todolist/', views.TodolistView.as_view(), name='todolist_view'),
    path('todolist/<int:todo_id>/', views.TodolistDetailView.as_view(), name='todolist_detail_view'),
]
