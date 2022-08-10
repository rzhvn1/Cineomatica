from rest_framework import permissions, viewsets

from .models import Feedback, FeedbackType
from .permissions import IsAdminUserOrReadOnly
from .serializers import FeedbackSerializer, FeedbackTypeSerializer


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
