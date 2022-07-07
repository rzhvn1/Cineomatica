from rest_framework import serializers
from .models import Order, TicketType, Ticket


class TicketTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = TicketType
        fields = ['id', 'name', 'price']

        extra_kwargs = {
            "name":{"required":True},
            "price":{"required":True}
        }

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['id', 'type', 'seats', 'show_time', 'order', 'price', 'payment_method', 'booking_by']

        extra_kwargs = {
            "type":{"required":True},
            "seats":{"required":True},
            "show_time":{"required":True},
            "order":{"required":False},
            "price":{"required":False},
            "payment_method":{"required":False},
            "booking_by":{"required":False}
        }

    def update(self, instance, validated_data):
        user = self.context['request'].user
        instance.booking_by = user
        if validated_data.get('payment_method'):
            order = Order.objects.create(user=user, total_price=instance.price)
            instance.order = order
        instance.save()
        return instance

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price']

        extra_kwargs = {
            "user":{"required":False},
            "total_price":{"required":False}
        }

