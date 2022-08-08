from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from account.models import CustomUser


class TestMovieSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_superuser(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "rzhvn", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("movie-list")

    def test_get_movie_upcoming_status_method(self):
        data = {
            "title": "Тор: Любовь и гром",
            "age_limit": 12,
            "start_date": "2023-08-01",
            "end_date": "2023-08-30",
        }
        self.movie = self.client.post(self.url, data, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_get_movie_current_status_method(self):
        data = {
            "title": "Тор: Любовь и гром",
            "age_limit": 12,
            "start_date": "2022-07-15",
            "end_date": "2022-08-15",
        }
        self.movie = self.client.post(self.url, data, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
