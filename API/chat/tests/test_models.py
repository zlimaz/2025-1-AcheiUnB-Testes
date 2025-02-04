from django.contrib.auth.models import User
from django.test import TestCase

from chat.models import ChatRoom, Message
from users.models import Item


class ChatRoomModelTests(TestCase):
    """Testes para o modelo ChatRoom."""

    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")
        self.item = Item.objects.create(name="Chave Perdida", status="lost")

    def test_create_chat_room(self):
        """Testa a criação de uma sala de chat."""
        chat_room = ChatRoom.objects.create(
            participant_1=self.user1, participant_2=self.user2, item=self.item
        )

        assert chat_room.participant_1 == self.user1
        assert chat_room.participant_2 == self.user2
        assert chat_room.item == self.item
        assert chat_room.created_at is not None

    def test_chat_room_str(self):
        """Testa a representação textual da sala de chat."""
        chat_room = ChatRoom.objects.create(
            participant_1=self.user1, participant_2=self.user2, item=self.item
        )
        expected_str = f"Chat between {self.user1.username} and {self.user2.username}"
        assert str(chat_room) == expected_str


class MessageModelTests(TestCase):
    """Testes para o modelo Message."""

    def setUp(self):
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")
        self.item = Item.objects.create(name="Carteira Perdida", status="lost")
        self.chat_room = ChatRoom.objects.create(
            participant_1=self.user1, participant_2=self.user2, item=self.item
        )

    def test_create_message(self):
        """Testa a criação de uma mensagem em um chat."""
        message = Message.objects.create(
            room=self.chat_room, sender=self.user1, content="Olá, encontrei seu item!"
        )

        assert message.room == self.chat_room
        assert message.sender == self.user1
        assert message.content == "Olá, encontrei seu item!"
        assert message.timestamp is not None

    def test_message_str(self):
        """Testa a representação textual de uma mensagem."""
        message = Message.objects.create(
            room=self.chat_room, sender=self.user1, content="Oi! Esta é uma mensagem de teste."
        )
        expected_str = "user1: Oi! Esta é uma mensagem de teste."
        assert str(message) == expected_str[:50]
