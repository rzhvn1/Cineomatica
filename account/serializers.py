from .models import CustomUser
from rest_framework import serializers


class CustomUserRegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "check_password",
            "address",
            "age",
            "phone",
        ]

        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True},
            "username": {"required": True},
            "email": {"required": True},
            "password": {"write_only": True},
            "address": {"required": False},
            "age": {"required": True},
            "phone": {"required": False},
        }

    def create(self, validated_data):
        if validated_data["password"] != validated_data["check_password"]:
            raise serializers.ValidationError("Passwords doesnt match!")
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            address=validated_data["address"],
            age=validated_data["age"],
            phone=validated_data["phone"],
        )
        user.save()
        return user