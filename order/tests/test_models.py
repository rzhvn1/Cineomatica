from django.test import TestCase
from ..models import Order, TicketType
from account.models import CustomUser

class TestOrderModel(TestCase):

    def test_str_method(self):
        user = CustomUser.objects.create_user(
            username="rzhvn", email="rzhvn@gmail.com", password="erzhan123", age=23
        )
        order = Order.objects.create(user=user)
        self.assertEqual(order.__str__(), f"{order.user}:{order.total_price}")

class TestTicketTypeModel(TestCase):

    def test_str_method(self):
        type = TicketType.objects.create(name="Student", price=50)
        self.assertEqual(type.__str__(), f"{type.name}:{type.price}")