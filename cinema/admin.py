from django.contrib import admin
from .models import Cinema, RoomType, Room, Seat

admin.site.register([Cinema, RoomType, Room, Seat])
