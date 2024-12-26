import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import ChatRoom, Message


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_id = self.scope['url_route']['kwargs']['room_id']
        self.room_group_name = f"chat_{self.room_id}"

        # Verifica se o usuário tem acesso à sala
        room = await sync_to_async(ChatRoom.objects.get)(id=self.room_id)
        user = self.scope['user']
        if user != room.participant_1 and user != room.participant_2:
            await self.close()
        else:
            await self.channel_layer.group_add(self.room_group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_content = data["message"]
        sender = self.scope["user"]

        # Salva a mensagem no banco
        room = await sync_to_async(ChatRoom.objects.get)(id=self.room_id)
        message = await sync_to_async(Message.objects.create)(
            room=room, sender=sender, content=message_content
        )

        # Envia a mensagem para o grupo
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message_content,
                "sender": sender.username,
                "timestamp": message.timestamp.isoformat(),
            },
        )

    async def chat_message(self, event):
        await self.send(
            text_data=json.dumps(
                {
                    "message": event["message"],
                    "sender": event["sender"],
                    "timestamp": event["timestamp"],
                }
            )
        )
