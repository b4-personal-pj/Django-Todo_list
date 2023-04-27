from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer
from users.models import User
# 세션 로그인
from django.contrib.auth import authenticate, login, logout



class UserView(APIView):
    def get (self, request):
        # 사용자 정보 보기
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        # 회원가입
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입을 환영합니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)
    def put (self, request):
        # 사용자 정보 수정
        pass
    def delete (self, request):
        # 회원 탈퇴
        pass

class LoginView(APIView):
    def post(self, request):
        user = authenticate(request, **request.data)
        if not user:
            return Response({"error": "존재하지 않는 유저입니다."}, status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        return Response({"message": "로그인 되었습니다."})
