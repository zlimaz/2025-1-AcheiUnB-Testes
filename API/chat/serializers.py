from rest_framework import serializers
from .models import ChatRoom, Message


class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.ReadOnlyField(source="sender.username")

    class Meta:
        model = Message
        fields = ["id", "room", "sender", "sender_username", "content", "timestamp"]
        read_only_fields = ["sender"]


class ChatRoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)
    participant_1_username = serializers.ReadOnlyField(source="participant_1.username")
    participant_2_username = serializers.ReadOnlyField(source="participant_2.username")

    class Meta:
        model = ChatRoom
        fields = [
            "id",
            "participant_1",
            "participant_1_username",
            "participant_2",
            "participant_2_username",
            "item_description",
            "created_at",
            "messages",
        ]
