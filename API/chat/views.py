from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from chat.models import ChatRoom, Message
from users.models import Item

from .serializers import ChatRoomSerializer, MessageSerializer


class ChatRoomViewSet(ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        participant_1_id = request.user.id
        participant_2_id = request.data.get("participant_2")
        item_id = request.data.get("item_id")

        if not participant_2_id or not item_id:
            raise ValidationError("Os campos participant_2 e item são obrigatórios.")

        if participant_1_id == int(participant_2_id):
            raise ValidationError("Não é possível criar um chat consigo mesmo.")

        if not Item.objects.filter(id=item_id).exists():
            raise ValidationError("O item associado não foi encontrado.")

        existing_chat = ChatRoom.objects.filter(
            participant_1=participant_1_id, participant_2=participant_2_id, item_id=item_id
        ).first()

        if existing_chat:
            return Response(self.get_serializer(existing_chat).data)

        return super().create(request, *args, **kwargs)


class MessageViewSet(ModelViewSet):
    """ViewSet para gerenciar mensagens."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        room_id = self.request.query_params.get("room")
        if room_id:
            return Message.objects.filter(room_id=room_id)
        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


class ClearChatsView(APIView):
    """Endpoint para limpar todas as mensagens e/ou salas de chat."""

    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        Message.objects.all().delete()
        ChatRoom.objects.all().delete()
        return Response({"detail": "Todos os chats foram limpos com sucesso."})
