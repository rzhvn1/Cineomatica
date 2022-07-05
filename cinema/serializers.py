from rest_framework import serializers
from .models import Cinema, Room

class CinemaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cinema
        fields = ['id', 'name', 'working_schedule', 'address', 'phone']

        extra_kwargs = {
            "name": {"required":True},
            "working_schedule": {"required":True},
            "address": {"required":True},
            "phone": {"required":True}
        }

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'name', 'type', 'cinema']

        extra_kwargs = {
            "name": {"required":True},
            "type": {"required":True},
            "cinema": {"required":True}
        }
