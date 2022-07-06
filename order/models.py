from django.db import models
from account.models import CustomUser

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user}:{self.total_price}"


