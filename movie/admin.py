from django.contrib import admin

from .models import AboutMovie, Movie, MovieFormat

admin.site.register([MovieFormat, Movie, AboutMovie])
