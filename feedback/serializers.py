from rest_framework import serializers
from .models import Feedback, FeedbackType


class FeedbackTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackType
        fields = ["id", "name"]

        extra_kwargs = {"name": {"required": True}}


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ["id", "user", "type", "text", "rate"]

        extra_kwargs = {
            "user": {"required": False},
            "type": {"required": True},
            "text": {"required": False},
            "rate": {"required": True},
        }
