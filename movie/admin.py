from django.contrib import admin
from .models import MovieFormat, Movie, AboutMovie

admin.site.register([MovieFormat, Movie, AboutMovie])
