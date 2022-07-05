from rest_framework import serializers
from .models import Movie, AboutMovie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ['id', 'title', 'age_limit', 'start_date', 'end_date']

        extra_kwargs = {
            "title": {"required":True},
            "age_limit": {"required":True},
            "start_date": {"required":True},
            "end_date": {"required":True},
        }
