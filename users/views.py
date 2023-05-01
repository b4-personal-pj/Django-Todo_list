from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer, UserUpdateSerializer
from users.models import User
from rest_framework.generics import get_object_or_404
'''세션 로그인, 로그아웃 모듈'''
from django.contrib.auth import authenticate, login, logout


class UserView(APIView):
    def get (self, request, user_id):
        '''사용자 정보 보기'''
        user = get_object_or_404(User, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        '''회원가입'''
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입을 환영합니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)
    def put (self, request, user_id):
        '''사용자 정보 수정'''
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            serializer = UserUpdateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

    def delete (self, request, user_id):
        '''회원 탈퇴'''
        user = get_object_or_404(User, id=user_id)
        if request.user == user:
            # user.delete() DB에서 삭제하면 안된다! 
            user.is_active = False
            user.save()
            return Response("삭제되었습니다.", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)

class LoginView(APIView):
    '''유저 로그인'''
    def post(self, request):
        user = authenticate(request, **request.data)
        if not user:
            return Response({"error": "존재하지 않는 유저입니다."}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        return Response({"message": "로그인 되었습니다."})
 
class LogoutView(APIView):
    '''유저 로그아웃'''
    def post(self, request):
        logout(request)
        return Response({"message": "로그아웃 되었습니다."})
        
