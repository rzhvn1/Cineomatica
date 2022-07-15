from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from account.models import CustomUser
from rest_framework import status
from ..models import Seat, Cinema, RoomType, Room


class TestSeatSerializer(APITestCase):

    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_superuser(username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23)
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "rzhvn", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("seat-list")

    def test_seat_create_method(self):
        # order = Order.objects.create(user=self.user, total_price=51000)
        # self.clubcard = self.client.post(self.url, {}, format='json')
        # self.response = self.client.get(self.url)
        cinema = Cinema.objects.create(name='Cosmopark')
        room_type = RoomType.objects.create(name="Demir", price=200)
        room = Room.objects.create(name="Hall 1", type=room_type, cinema=cinema)
        data = {
                "row_number":4,
                "seat_number":4,
                "room":room.id
            }
        self.response = self.client.post(self.url, data, format='json')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
