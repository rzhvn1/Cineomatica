from rest_framework import viewsets, permissions
from .serializers import OrderSerializer, TicketTypeSerializer, TicketSerializer
from .models import Order, TicketType, Ticket
from .permissions import IsAdminUserOrReadOnly
from django.db.models.functions import TruncMonth
from django.db.models import Sum


class OrderModelViewSet(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return (
                Order.objects.annotate(month=TruncMonth("created"))
                .values("month")
                .annotate(total_income=Sum("total_price"))
                .values("month", "total_income")
            )
        return Order.objects.filter(user=self.request.user)


class TicketTypeModelViewSet(viewsets.ModelViewSet):

    serializer_class = TicketTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = TicketType.objects.all()


class TicketModelViewSet(viewsets.ModelViewSet):
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Ticket.objects.all()
