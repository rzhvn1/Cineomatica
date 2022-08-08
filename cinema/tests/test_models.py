from django.test import TestCase
from ..models import Cinema, RoomType, Room, Seat


class TestCinemaModel(TestCase):
    def test_str_method(self):
        cinema = Cinema.objects.create(name="Cosmopark")
        self.assertEqual(cinema.__str__(), cinema.name)


class TestRoomTypeModel(TestCase):
    def test_str_method(self):
        room_type = RoomType.objects.create(name="Demir", price=200)
        self.assertEqual(room_type.__str__(), f"{room_type.name}:{room_type.price}")


class TestRoomModel(TestCase):
    def test_property_seats_method(self):
        cinema = Cinema.objects.create(name="Cosmopark")
        room_type = RoomType.objects.create(name="Demir", price=200)
        room = Room.objects.create(name="Hall 1", type=room_type, cinema=cinema)
        seat = Seat.objects.create(row_number=1, seat_number=1, room=room)
        property_method = room.seats[0].id
        self.assertEqual(property_method, seat.id)
