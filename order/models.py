from django.db import models
from account.models import CustomUser
from cinema.models import Seat
from movie.models import ShowTime


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.PositiveIntegerField(default=0, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}:{self.total_price}"


class TicketType(models.Model):
    name = models.CharField(max_length=55, unique=True)
    price = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}:{self.price}"


class Ticket(models.Model):
    methods = [
        (1, "Credit Card"),
        (2, "Balance.kg"),
        (3, "Элсом"),
        (4, "О! Деньги"),
        (5, "Megapay"),
    ]
    type = models.ForeignKey(
        TicketType, on_delete=models.CASCADE, related_name="tickettype"
    )
    seats = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name="seats")
    show_time = models.ForeignKey(
        ShowTime, on_delete=models.CASCADE, related_name="showtime"
    )
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, blank=True, null=True, related_name="order"
    )
    price = models.PositiveIntegerField(default=0)
    payment_method = models.IntegerField(choices=methods, blank=True, null=True)
    booking_by = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, blank=True, null=True
    )

    def save(self, *args, **kwargs):
        if (
            self.type.name == "Child"
            or self.type.name == "Adult"
            or self.type.name == "Student"
            and self.show_time.movie_format.name == "2-D"
            or self.show_time.movie_format.name == "3-D"
            and self.seats.room.type.name == "Зал 1"
            or self.seats.room.type.name == "Зал 2"
            or self.seats.room.type.name == "Зал 3"
            or self.seats.room.type.name == "IMAX"
        ):
            self.price = (
                self.type.price
                + self.show_time.movie_format.price
                + self.seats.room.type.price
            )
        super().save(*args, **kwargs)
