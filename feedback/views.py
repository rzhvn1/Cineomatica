from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import FeedbackSerializer, FeedbackTypeSerializer
from .models import Feedback, FeedbackType
from .permissions import IsAdminUserOrReadOnly


class FeedbackTypeModelViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = FeedbackType.objects.all()


class FeedbackModelViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Feedback.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
