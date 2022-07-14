from django.contrib import admin
from .models import CustomUser, ClubCard

admin.site.register([CustomUser, ClubCard])
