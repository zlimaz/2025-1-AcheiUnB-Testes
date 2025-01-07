from django.db import models  # Certifique-se de importar models para usar Q
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from chat.models import ChatRoom, Message

from .serializers import ChatRoomSerializer, MessageSerializer


class ChatRoomViewSet(ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        participant_1 = request.data.get("participant_1")
        participant_2 = request.data.get("participant_2")

        # Verifica se a sala já existe
        if ChatRoom.objects.filter(
            (
                models.Q(participant_1=participant_1, participant_2=participant_2)
                | models.Q(participant_1=participant_2, participant_2=participant_1)
            )
        ).exists():
            raise ValidationError("Já existe um chat entre esses participantes.")

        return super().create(request, *args, **kwargs)


class MessageViewSet(ModelViewSet):
    """ViewSet para gerenciar mensagens."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Obtém o parâmetro "room" da URL (query params)
        room_id = self.request.query_params.get("room")
        if room_id:
            return Message.objects.filter(room_id=room_id)
        return super().get_queryset()

    def perform_create(self, serializer):
        # O remetente da mensagem será sempre o usuário autenticado
        serializer.save(sender=self.request.user)


class ClearChatsView(APIView):
    """Endpoint para limpar todas as mensagens e/ou salas de chat."""

    permission_classes = [IsAdminUser]

    def delete(self, request, *args, **kwargs):
        # Apaga mensagens e salas de chat
        Message.objects.all().delete()
        ChatRoom.objects.all().delete()
        return Response({"detail": "Todos os chats foram limpos com sucesso."})
