from rest_framework import serializers
from todos.models import Todo

class TodolistSerializer (serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Todo
        fields = "__all__"