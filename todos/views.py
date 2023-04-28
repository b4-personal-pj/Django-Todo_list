from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from todos.serializers import TodolistSerializer
from todos.models import Todo
from rest_framework.generics import get_object_or_404


class TodolistView(APIView):
    def get (self, request):
        '''할 일 조회'''
        todolist = Todo.objects.all() # 일단 전부
        serializer = TodolistSerializer(todolist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post (self, request):
        '''할 일 작성'''
        serializer = TodolistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put (self, request, todo_id):
        '''할 일 수정'''
        pass
    
    def delete (self, request, todo_id):
        '''할 일 삭제'''
        pass
