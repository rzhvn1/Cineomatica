from django.test import TestCase
from ..models import CustomUser, ClubCard


class TestCustomUserModel(TestCase):
    def test_str_method(self):
        user = CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        self.assertEqual(user.__str__(), user.username)


class TestClubCardModel(TestCase):
    def test_str_method(self):
        user = CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        clubcard = ClubCard.objects.create(user=user)
        self.assertEqual(clubcard.__str__(), f"{clubcard.balance}")
