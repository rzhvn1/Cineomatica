from django.db import models

class Cinema(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    working_schedule = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=55, blank=True, null=True)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=55, unique=True)
    price = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}:{self.price}"

class Room(models.Model):
    name = models.CharField(max_length=55, unique=True)
    type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)

class Seat(models.Model):
    row_number = models.PositiveIntegerField(blank=True, null=True)
    seat_number = models.PositiveIntegerField(blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="seat")
    