from django.db import models

from account.models import CustomUser


class FeedbackType(models.Model):
    name = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    rate_choices = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type = models.ForeignKey(FeedbackType, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    rate = models.IntegerField(choices=rate_choices)
