from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (OrderModelViewSet, TicketModelViewSet,
                    TicketTypeModelViewSet)

router = DefaultRouter()
router.register(r"ticket", TicketModelViewSet, basename="ticket")
router.register(r"ticket-type", TicketTypeModelViewSet, basename="ticket-type")
router.register(r"", OrderModelViewSet, basename="order")


urlpatterns = [
    path("", include(router.urls)),
]
