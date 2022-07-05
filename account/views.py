from django.shortcuts import render
from rest_framework import mixins, viewsets, permissions, status, views, generics
from rest_framework.response import Response
from .models import CustomUser
from .serializers import CustomUserRegisterSerializer, ChangePasswordSerializer, LogoutSerializer


class CustomUserRegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = CustomUserRegisterSerializer
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.AllowAny]

class UpdatePassword(views.APIView):

    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, queryset=None):
        return self.request.user

    def put(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            old_password = serializer.data.get("old_password")
            if not self.object.check_password(old_password):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(
                {"Password changed successfully"}, status=status.HTTP_204_NO_CONTENT
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"Logged out successfully!"}, status=status.HTTP_204_NO_CONTENT)
