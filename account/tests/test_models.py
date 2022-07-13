from django.test import TestCase
from ..models import CustomUser


class TestCustomUserModel(TestCase):

    def test_str_method(self):
        user = CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        self.assertEqual(user.__str__(), user.username)