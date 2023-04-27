from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer, UserUpdateSerializer
from users.models import User
from rest_framework.generics import get_object_or_404


class TodolistView(APIView):
    def get (self, request, todo_id):
        '''할 일 조회'''
        pass
    
    def post (self, request, todo_id):
        '''할 일 작성'''
        pass

    def put (self, request, todo_id):
        '''할 일 수정'''
        pass
    
    def delete (self, request, todo_id):
        '''할 일 삭제'''
        pass
