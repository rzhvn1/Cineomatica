import datetime
from rest_framework import viewsets, permissions
from .serializers import MovieSerializer
from .permissions import IsAdminUserOrReadOnly
from .models import Movie

class MovieModelViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    permission_classes = [IsAdminUserOrReadOnly]

    def get_queryset(self):
        return Movie.objects.filter(end_date__gt=datetime.datetime.now())
    

