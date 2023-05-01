from rest_framework import serializers
from users.models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ("email", "name", "gender", "age", "introduction")
        # password 안보이도록 수정했지만 이렇게 하면 로그인이 안됨!! 
        # 다른 방법
        fields = "__all__"
        extra_kwargs = {
            "password":{
                "write_only": True,
            },
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class UserUpdateSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name", "gender", "age", "introduction")