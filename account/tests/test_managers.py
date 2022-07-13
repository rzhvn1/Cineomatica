from ..models import CustomUser
from django.test import TestCase


class TestCustomUserManager(TestCase):

    def test_create_user_method(self):
        user = CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        self.assertTrue(isinstance(user, CustomUser))

    def test_create_superuser_method(self):
        user = CustomUser.objects.create_superuser(
            username="rzhvn",
            email="rzhvn@gmail.com",
            password="erzhan123",
            age=23,
            is_superuser=True,
            is_staff=True,
        )
        self.assertTrue(isinstance(user, CustomUser))

    def test_create_user_username_is_not_set(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(username=None, email="rzhvn@gmail.com", password="erzhan123", age=23)

    def test_create_user_email_is_not_set(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(username="rzhvn", email=None, password="erzhan123", age=23)

    def test_create_user_password_is_not_set(self):

        with self.assertRaises(ValueError):
            CustomUser.objects.create_user(username="rzhvn", email="rzhvn@gmail.com", password=None, age=23)

    def test_create_superuser_is_superuser_is_not_true(self):

        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                username="rzhvn",
                email="rzhvn@gmail.com",
                password="erzhan123",
                age = 23,
                is_superuser=False,
                is_staff=True
            )

    def test_create_superuser_is_staff_is_not_true(self):

        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                username="rzhvn",
                email="rzhvn@gmail.com",
                password="erzhan123",
                age=23,
                is_superuser=True,
                is_staff=False,
            )

    def test_create_superuser_is_superuser_and_is_staff_is_not_true(self):
        with self.assertRaises(ValueError):
            CustomUser.objects.create_superuser(
                username="rzhvn",
                email="rzhvn@gmail.com",
                password="erzhan123",
                age=23,
                is_superuser=False,
                is_staff=False,
            )