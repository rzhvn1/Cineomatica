from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase

from order.models import Order

from ..models import CustomUser


class TestCustomUserRegisterSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("register-list")
        CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )

    def test_user_create_successfully(self):
        data = {
            "username": "rzhvn1",
            "first_name": "Erzhan",
            "last_name": "Muratov",
            "email": "rzhvn1@gmail.com",
            "password": "erzhan123",
            "check_password": "erzhan123",
            "address": "Neobis",
            "age": 23,
            "phone": "+123456789",
        }
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_if_passwords_does_not_match(self):
        data = {
            "username": "rzhvn1",
            "first_name": "Erzhan",
            "last_name": "Muratov",
            "email": "rzhvn1@gmail.com",
            "password": "erzhan123",
            "check_password": "erzhan",
            "address": "Neobis",
            "age": 23,
            "phone": "+123456789",
        }
        self.response = self.client.post(self.url, data, format="json")
        self.assertContains(
            self.response, text="Passwords doesnt match!", status_code=400
        )


class TestChangePasswordSerializer(APITestCase):
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

    def test_password_changed_successfully(self):
        data = {"old_password": "erzhan123", "new_password": "admin123456"}
        self.response = self.client.put(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)


class TestLogoutSerializer(APITestCase):
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
        self.url = reverse("auth_logout")

    def test_logout_successfully(self):
        refresh_token = self.res.data["refresh"]
        data = {"refresh": refresh_token}
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)

    def test_logout_invalid_token(self):
        data = {"refresh": "1"}
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)


class TestClubCardSerializer(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        self.res = self.client.post(
            reverse("token_obtain_pair"),
            {"username": "rzhvn", "password": "erzhan123"},
        )
        access_token = self.res.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + access_token)

        self.url = reverse("club-card-list")

    def test_club_card_get_balance_over_50000(self):
        Order.objects.create(user=self.user, total_price=51000)
        self.clubcard = self.client.post(self.url, {}, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_club_card_get_balance_over_75000(self):
        Order.objects.create(user=self.user, total_price=76000)
        self.clubcard = self.client.post(self.url, {}, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_club_card_get_balance_over_100000(self):
        Order.objects.create(user=self.user, total_price=101000)
        self.clubcard = self.client.post(self.url, {}, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
