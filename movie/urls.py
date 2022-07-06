from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieModelViewSet, AboutMovieModelViewSet, ShowTimeModelViewSet, MovieFormatModelViewSet

router = DefaultRouter()
router.register(r"movie-format", MovieFormatModelViewSet, basename='movie-format')
router.register(r"showtime", ShowTimeModelViewSet, basename="showtime")
router.register(r"about-movie", AboutMovieModelViewSet, basename="about-movie")
router.register(r"", MovieModelViewSet, basename="movie")


urlpatterns = [
    path("", include(router.urls)),
]