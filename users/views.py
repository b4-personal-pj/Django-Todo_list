from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer

# Create your views here.

# 회원가입
class UserCreateView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"가입을 환영합니다."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":f"${serializer.errors}"},status=status.HTTP_400_BAD_REQUEST)