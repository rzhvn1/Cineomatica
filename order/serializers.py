from rest_framework import serializers
from .models import Order, TicketType

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price']

        extra_kwargs = {
            "user":{"required":False},
            "total_price":{"required":False}
        }

class TicketTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketType
        fields = ['id', 'name', 'price']

        extra_kwargs = {
            "name":{"required":True},
            "price":{"required":True}
        }

