from rest_framework.test import APITestCase, APIClient
from rest_framework.reverse import reverse
from rest_framework import status
from ..models import FeedbackType
from account.models import CustomUser


class TestFeedbackModelViewSet(APITestCase):
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
        self.url = reverse("feedback-list")

    def test_perform_create_method(self):
        type = FeedbackType.objects.create(name="Suggestion")
        data = {"type": type.id, "text": "I Love your IMAX!!!", "rate": 5}
        self.response = self.client.post(self.url, data, format="json")
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_get_queryset_method(self):
        type = FeedbackType.objects.create(name="Suggestion")
        data = {"type": type.id, "text": "I Love your IMAX!!!", "rate": 5}
        self.feedback = self.client.post(self.url, data, format="json")
        self.response = self.client.get(self.url)
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
