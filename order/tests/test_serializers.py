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
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "rzhvn", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("ticket-list")

    def test_validate_method(self):
        pass