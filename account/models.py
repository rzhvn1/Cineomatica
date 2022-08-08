from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(verbose_name="email", max_length=255, unique=True)
    first_name = models.CharField(max_length=255, verbose_name="first_name")
    last_name = models.CharField(max_length=255, verbose_name="last_name")
    address = models.CharField(
        max_length=255, verbose_name="address", null=True, blank=True
    )
    age = models.PositiveIntegerField(verbose_name="age")
    phone = models.CharField(
        max_length=255, verbose_name="phone", null=True, blank=True
    )

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "age"]

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class ClubCard(models.Model):
    balance = models.IntegerField(default=0)
    discount = models.FloatField(default=0.1)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.balance}"
