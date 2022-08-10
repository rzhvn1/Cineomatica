from django.contrib import admin

from .models import ClubCard, CustomUser

admin.site.register([CustomUser, ClubCard])
