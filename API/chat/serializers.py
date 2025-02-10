from rest_framework import serializers

from users.models import Item

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
    item_id = serializers.IntegerField(write_only=True, required=True)
    item_name = serializers.ReadOnlyField(source="item.name")

    class Meta:
        model = ChatRoom
        fields = [
            "id",
            "participant_1",
            "participant_1_username",
            "participant_2",
            "participant_2_username",
            "item_id",
            "item_name",
            "created_at",
            "messages",
        ]

    def validate_item_id(self, value):
        # Verifica se o item associado existe
        if not Item.objects.filter(id=value).exists():
            raise serializers.ValidationError("O item associado não foi encontrado.")
        return value

    def create(self, validated_data):
        # Associa o item ao chat usando o item_id
        item_id = validated_data.pop("item_id")
        validated_data["item"] = Item.objects.get(id=item_id)

        # Criação do chat
        chat_room = super().create(validated_data)
        return chat_room
