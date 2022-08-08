from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, ClubCard
from order.models import Order
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken, TokenError


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


class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        validate_password(value)
        return value


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_messages = {"bad_token": ("Token is expired or invalid")}

    def validate(self, attrs):
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail("bad_token")


class ClubCardSerializer(serializers.ModelSerializer):

    balance = serializers.SerializerMethodField()

    class Meta:
        model = ClubCard
        fields = ["id", "balance", "discount", "user"]

        extra_kwargs = {
            "balance": {"required": False},
            "discount": {"required": False},
            "user": {"required": False},
        }

    def get_balance(self, obj):
        orders = Order.objects.filter(user=obj.user)
        balance = 0
        for i in orders:
            balance += i.total_price
            if balance > 50000:
                obj.discount = 0.15
            if balance > 75000:
                obj.discount = 0.2
            if balance > 100000:
                obj.discount = 0.3
        obj.save()
        return balance
