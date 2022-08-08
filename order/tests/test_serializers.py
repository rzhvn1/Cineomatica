from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from account.models import CustomUser
from ..models import Ticket, TicketType
from cinema.models import Cinema, Room, RoomType, Seat
from movie.models import Movie, MovieFormat, ShowTime



class TestTicketSerializer(APITestCase):

    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_superuser(username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23)
        CustomUser.objects.create_superuser(username="rzhvn1", email="rzhvn1@gmail.com", password="erzhan123",
                                                   age=23)
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "rzhvn", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("ticket-list")

    def test_validate_method(self):
        type = TicketType.objects.create(name="Child", price=50)
        cinema = Cinema.objects.create(name='Cosmopark')
        room_type = RoomType.objects.create(name="Demir", price=200)
        room = Room.objects.create(name="Hall 1", type=room_type, cinema=cinema)
        seat = Seat.objects.create(row_number=1, seat_number=1, room=room)
        movie = Movie.objects.create(title="Mad Max 3", age_limit=18, start_date="2022-07-19", end_date="2022-08-19")
        movie_format = MovieFormat.objects.create(name="3-D", price=100)
        show_time = ShowTime.objects.create(movie=movie, movie_format=movie_format, room=room, start_time="2022-07-30",
                                            end_time="2022-08-30")
        ticket = Ticket.objects.create(type=type, seats=seat, show_time=show_time)

        data1 = {
            "type":type.id,
            "seats":seat.id,
            "show_time":show_time.id
        }
        self.repsonse1 = self.client.put(f"{self.url}{ticket.id}/", data1, format='json')
        data2 = {
            "type": type.id,
            "seats": seat.id,
            "show_time": show_time.id
        }
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "rzhvn1", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.response2 = self.client.put(f"{self.url}{ticket.id}/", data2, format='json')
        self.assertContains(self.response2, text="This seat is already reserved!", status_code=400)

    def test_update_method(self):
        type = TicketType.objects.create(name="Child", price=50)
        cinema = Cinema.objects.create(name='Cosmopark')
        room_type = RoomType.objects.create(name="Demir", price=200)
        room = Room.objects.create(name="Hall 1", type=room_type, cinema=cinema)
        seat = Seat.objects.create(row_number=1, seat_number=1, room=room)
        movie = Movie.objects.create(title="Mad Max 3", age_limit=18, start_date="2022-07-19", end_date="2022-08-19")
        movie_format = MovieFormat.objects.create(name="3-D", price=100)
        show_time = ShowTime.objects.create(movie=movie, movie_format=movie_format, room=room, start_time="2022-07-30",
                                            end_time="2022-08-30")
        ticket = Ticket.objects.create(type=type, seats=seat, show_time=show_time)

        data = {
            "type": type.id,
            "seats": seat.id,
            "show_time": show_time.id,
            "payment_method":1
        }
        self.repsonse = self.client.put(f"{self.url}{ticket.id}/", data, format='json')
        self.assertEqual(self.repsonse.status_code, status.HTTP_200_OK)