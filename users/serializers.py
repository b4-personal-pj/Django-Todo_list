from rest_framework import serializers
from users.models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        fields = ("email", "name", "gender", "age", "introduction")
        # password 안보이도록 수정

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