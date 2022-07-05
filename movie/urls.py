from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieModelViewSet, AboutMovieModelViewSet

router = DefaultRouter()
router.register(r"about-movie", AboutMovieModelViewSet, basename="about-movie")
router.register(r"", MovieModelViewSet, basename="movie")


urlpatterns = [
    path("", include(router.urls)),
]