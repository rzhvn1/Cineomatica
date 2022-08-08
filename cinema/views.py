from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Cinema, Room, Seat, RoomType
from .serializers import (
    CinemaSerializer,
    RoomSerializer,
    SeatSerializer,
    RoomTypeSerializer,
)
from .permissions import IsAdminUserOrReadOnly


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
