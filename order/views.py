from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import OrderSerializer, TicketTypeSerializer
from .models import Order, TicketType
from .permissions import IsAdminUserOrReadOnly

class OrderModelViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class TicketTypeModelViewSet(viewsets.ModelViewSet):

    serializer_class = TicketTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = TicketType.objects.all()

