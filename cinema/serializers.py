from rest_framework import serializers
from .models import Cinema, Room, Seat

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

class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = ['id', 'row_number', 'seat_number', 'room']

        extra_kwargs = {
            "row_number": {"required":True},
            "seat_number": {"required":True},
            "room": {"required":True}
        }

class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = ['id', 'name', 'type', 'cinema', 'seats']

        extra_kwargs = {
            "name": {"required":True},
            "type": {"required":True},
            "cinema": {"required":True}
        }



