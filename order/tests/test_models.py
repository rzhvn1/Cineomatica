from django.test import TestCase
from ..models import Order, TicketType, Ticket
from account.models import CustomUser
from cinema.models import Seat, Cinema, RoomType, Room
from movie.models import ShowTime, Movie, MovieFormat

class TestOrderModel(TestCase):

    def test_str_method(self):
        user = CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        order = Order.objects.create(user=user)
        self.assertEqual(order.__str__(), f"{order.user}:{order.total_price}")

class TestTicketTypeModel(TestCase):

    def test_str_method(self):
        type = TicketType.objects.create(name="Student", price=50)
        self.assertEqual(type.__str__(), f"{type.name}:{type.price}")

class TestTicketModel(TestCase):

    def test_save_method(self):
        type = TicketType.objects.create(name="Child", price=50)
        cinema = Cinema.objects.create(name='Cosmopark')
        room_type = RoomType.objects.create(name="Demir", price=200)
        room = Room.objects.create(name="Hall 1", type=room_type, cinema=cinema)
        seat = Seat.objects.create(row_number=1, seat_number=1, room=room)
        movie = Movie.objects.create(title="Mad Max 3", age_limit=18, start_date="2022-07-19", end_date="2022-08-19")
        movie_format = MovieFormat.objects.create(name="3-D", price=100)
        show_time = ShowTime.objects.create(movie=movie, movie_format=movie_format, room=room, start_time="2022-07-30", end_time="2022-08-30")
        ticket = Ticket.objects.create(type=type, seats=seat, show_time=show_time)
        self.assertEqual(ticket.price, type.price+show_time.movie_format.price+seat.room.type.price)

