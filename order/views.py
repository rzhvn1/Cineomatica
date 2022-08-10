from django.db.models import Sum
from django.db.models.functions import TruncMonth
from rest_framework import permissions, viewsets

from .models import Order, Ticket, TicketType
from .permissions import IsAdminUserOrReadOnly
from .serializers import (OrderSerializer, TicketSerializer,
                          TicketTypeSerializer)


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
