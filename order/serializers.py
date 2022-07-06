from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price']

        extra_kwargs = {
            "user":{"required":False},
            "total_price":{"required":False}
        }

