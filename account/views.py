from django.shortcuts import render
from rest_framework import mixins, viewsets, permissions
from .models import CustomUser
from .serializers import CustomUserRegisterSerializer


class CustomUserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CustomUserRegisterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]
