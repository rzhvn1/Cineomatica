from rest_framework import serializers
from .models import Feedback

class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = Feedback
        fields = ['id', 'user', 'type', 'text', 'rate']

        extra_kwargs = {
            "user": {"required":False},
            "type": {"required":True},
            "text": {"required":False},
            "rate": {"required":True}
        }