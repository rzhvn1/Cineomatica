from django.contrib import admin

from .models import Cinema, Room, RoomType, Seat

admin.site.register([Cinema, RoomType, Room, Seat])
