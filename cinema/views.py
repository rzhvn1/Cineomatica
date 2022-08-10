from rest_framework import viewsets

from .models import Cinema, Room, RoomType, Seat
from .permissions import IsAdminUserOrReadOnly
from .serializers import (CinemaSerializer, RoomSerializer, RoomTypeSerializer,
                          SeatSerializer)


class CinemaModelViewSet(viewsets.ModelViewSet):
    serializer_class = CinemaSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Cinema.objects.all()


class RoomTypeModelViewSet(viewsets.ModelViewSet):
    serializer_class = RoomTypeSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = RoomType.objects.all()


class RoomModelViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Room.objects.all()


class SeatModelViewSet(viewsets.ModelViewSet):
    serializer_class = SeatSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Seat.objects.all()
