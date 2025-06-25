from rest_framework import serializers
from .models import Message

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

    def validate(self, data):
        if not data.get("recipient_number") or not data.get("message_text"):
            raise serializers.ValidationError("Both number and message are required.")
        return data

        