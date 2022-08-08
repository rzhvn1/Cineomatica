from rest_framework import serializers
from .models import Order, TicketType, Ticket


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = ["id", "name", "price"]

        extra_kwargs = {"name": {"required": True}, "price": {"required": True}}


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "id",
            "type",
            "seats",
            "show_time",
            "order",
            "price",
            "payment_method",
            "booking_by",
        ]

        extra_kwargs = {
            "type": {"required": True},
            "seats": {"required": True},
            "show_time": {"required": True},
            "order": {"required": False},
            "price": {"required": False},
            "payment_method": {"required": False},
            "booking_by": {"required": False},
        }

    def validate(self, attrs):
        try:
            ticket_pk = self.context["view"].kwargs["pk"]
        except:
            return attrs
        ticket = Ticket.objects.get(pk=ticket_pk)
        if not ticket.booking_by or ticket.booking_by == self.context["request"].user:
            return attrs
        raise serializers.ValidationError("This seat is already reserved!")

    def update(self, instance, validated_data):
        user = self.context["request"].user
        instance.booking_by = user
        if validated_data.get("payment_method"):
            instance.payment_method = validated_data.get(
                "payment_method", instance.payment_method
            )
            order = Order.objects.create(user=user, total_price=instance.price)
            instance.order = order
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):

    movie = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = ["id", "user", "total_price", "movie"]

        extra_kwargs = {"user": {"required": False}, "total_price": {"required": False}}

    def to_representation(self, instance):
        user = self.context["request"].user
        if user.is_superuser:
            representation = {
                "month": instance["month"],
                "total_income": instance["total_income"],
            }
            return representation
        else:
            orders = Order.objects.filter(user=user)
            for order in orders:
                try:
                    ticket = Ticket.objects.get(order=order)
                except:
                    raise serializers.ValidationError("No tickets")
                instance.movie = ticket.show_time.movie.title
            representation = {
                "id": instance.id,
                "user": instance.user.id,
                "total_price": instance.total_price,
                "movie": instance.movie,
            }
            return representation
