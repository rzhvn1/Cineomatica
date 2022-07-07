from django.db import models
from account.models import CustomUser

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user}:{self.total_price}"

class TicketType(models.Model):
    name = models.CharField(max_length=55, unique=True)
    price = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}:{self.price}"


