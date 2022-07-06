from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CinemaModelViewSet, RoomModelViewSet, SeatModelViewSet

router = DefaultRouter()
router.register(r"seat", SeatModelViewSet, basename="seat")
router.register(r"room", RoomModelViewSet, basename="room")
router.register(r"", CinemaModelViewSet, basename="cinema")

urlpatterns = [
    path("", include(router.urls)),
]