from rest_framework import serializers
from .models import Cinema, Room, Seat, RoomType


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = ["id", "name", "working_schedule", "address", "phone"]

        extra_kwargs = {
            "name": {"required": True},
            "working_schedule": {"required": True},
            "address": {"required": True},
            "phone": {"required": True},
        }


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ["id", "row_number", "seat_number", "room"]

        extra_kwargs = {
            "row_number": {"required": True},
            "seat_number": {"required": True},
            "room": {"required": True},
        }

    # creating matrix of seats
    def create(self, validated_data):
        global seats
        row_number = validated_data.pop("row_number")
        seat_number = validated_data.pop("seat_number")
        for row in range(1, row_number + 1):
            for seat in range(1, seat_number + 1):
                seats = Seat.objects.create(
                    row_number=row, seat_number=seat, **validated_data
                )
        return seats


class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomType
        fields = ["id", "name", "price"]

        extra_kwargs = {"name": {"required": True}, "price": {"required": True}}


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ["id", "name", "type", "cinema"]

        extra_kwargs = {
            "name": {"required": True},
            "type": {"required": True},
            "cinema": {"required": True},
        }
