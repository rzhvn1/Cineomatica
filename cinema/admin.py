from django.contrib import admin
from .models import Cinema, RoomType, Room

admin.site.register([Cinema, RoomType, Room])
