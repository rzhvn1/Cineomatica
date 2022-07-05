from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieModelViewSet

router = DefaultRouter()
router.register(r"", MovieModelViewSet, basename="movie")

urlpatterns = [
    path("", include(router.urls)),
]