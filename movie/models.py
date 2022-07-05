from django.db import models
from django.utils import timezone

class MovieFormat(models.Model):
    name = models.CharField(max_length=55, unique=True)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}:{self.price}"

class Movie(models.Model):
    title = models.CharField(max_length=100)
    age_limit = models.IntegerField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.title

class AboutMovie(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    year = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)
    actor = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

