from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from todos.serializers import TodolistSerializer, TodolistDetailSerializer
from todos.models import Todo
from rest_framework.generics import get_object_or_404


class TodolistView(APIView):
    def get (self, request):
        '''모든 할 일 조회'''
        todolist = Todo.objects.all() 
        serializer = TodolistSerializer(todolist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post (self, request):
        '''할 일 작성'''
        serializer = TodolistDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''본인만 가능'''
class TodolistDetailView(APIView):
    def get(self, request, todo_id):
        '''특정 할 일 조회'''
        todolist = get_object_or_404(Todo, id=todo_id)
        if request.user == todolist.user:
            serializer = TodolistDetailSerializer(todolist)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response("열람할 수 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def put (self, request, todo_id):
        '''할 일 수정'''
        todolist = get_object_or_404(Todo, id=todo_id)
        if request.user == todolist.user:
            serializer = TodolistDetailSerializer(todolist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("본인만 수정이 가능합니다.", status=status.HTTP_403_FORBIDDEN)
        
    def delete (self, request, todo_id):
        '''할 일 삭제'''
        todolist = get_object_or_404(Todo, id=todo_id)
        if request.user == todolist.user:
            todolist.delete()
            return Response("할 일을 삭제했습니다.", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("본인만 삭제할 수 있습니다.", status=status.HTTP_403_FORBIDDEN)
