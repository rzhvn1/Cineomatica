from rest_framework import serializers
from .models import Movie, AboutMovie, ShowTime, MovieFormat
import datetime


class MovieFormatSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieFormat
        fields = ["id", "name", "price"]

        extra_kwargs = {"name": {"required": True}, "price": {"required": True}}


class AboutMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutMovie
        fields = [
            "id",
            "movie",
            "title",
            "description",
            "year",
            "director",
            "genre",
            "actor",
            "country",
        ]

        extra_kwargs = {
            "movie": {"required": True},
            "title": {"required": True},
            "description": {"required": True},
            "year": {"required": True},
            "director": {"required": True},
            "genre": {"required": True},
            "actor": {"required": True},
            "country": {"required": True},
        }


class MovieSerializer(serializers.ModelSerializer):

    movie_status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = ["id", "title", "age_limit", "start_date", "end_date", "movie_status"]

        extra_kwargs = {
            "title": {"required": True},
            "age_limit": {"required": True},
            "start_date": {"required": True},
            "end_date": {"required": True},
            "movie_status": {"required": False},
        }

    @staticmethod
    def get_movie_status(obj):
        now = datetime.date.today()
        if obj.start_date <= now <= obj.end_date:
            obj.movie_status = "Current"
            return obj.movie_status
        if obj.start_date > now:
            obj.movie_status = "Upcoming"
            return obj.movie_status


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = ["id", "movie", "movie_format", "room", "start_time", "end_time"]

        extra_kwargs = {
            "movie": {"required": True},
            "movie_format": {"required": True},
            "room": {"required": True},
            "start_time": {"required": True},
            "end_time": {"required": True},
        }
