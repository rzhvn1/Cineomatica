from django.test import TestCase
from ..models import FeedbackType


class TestFeedbackTypeModel(TestCase):

    def test_str_method(self):
        type = FeedbackType.objects.create(name="Suggestion")
        self.assertEqual(type.__str__(), type.name)
