import datetime
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer, AboutMovieSerializer, ShowTimeSerializer, MovieFormatSerializer
from .permissions import IsAdminUserOrReadOnly
from .models import Movie, AboutMovie, ShowTime, MovieFormat

class MovieModelViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        return Movie.objects.filter(end_date__gt=datetime.datetime.now())

class MovieFormatModelViewSet(viewsets.ModelViewSet):
    serializer_class = MovieFormatSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = MovieFormat.objects.all()

class AboutMovieModelViewSet(viewsets.ModelViewSet):
    serializer_class = AboutMovieSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = AboutMovie.objects.all()

class ShowTimeModelViewSet(viewsets.ModelViewSet):
    serializer_class = ShowTimeSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = ShowTime.objects.all()




