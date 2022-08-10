from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from ..models import CustomUser


class TestUpdatePassword(APITestCase):
    def setUp(self):
        self.client = APIClient()
        CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "rzhvn", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)
        self.url = reverse("change-password")

    def test_wrong_old_password(self):
        data = {"old_password": "wrong", "new_password": "admin123456"}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_serializer_is_not_valid(self):
        data = {}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)
