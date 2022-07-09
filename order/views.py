from rest_framework import viewsets, permissions
from .serializers import OrderSerializer, TicketTypeSerializer, TicketSerializer
from .models import Order, TicketType, Ticket
from .permissions import IsAdminUserOrReadOnly

class OrderModelViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)

class TicketTypeModelViewSet(viewsets.ModelViewSet):

    serializer_class = TicketTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = TicketType.objects.all()

class TicketModelViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
