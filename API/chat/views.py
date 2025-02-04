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
        participant_1_id = request.data.get("participant_1")
        participant_2_id = request.data.get("participant_2")
        item_id = request.data.get("item_id")

        # Verifica se todos os dados necessários foram fornecidos
        if not participant_1_id or not participant_2_id or not item_id:
            raise ValidationError(
                "Os campos participant_1, participant_2 e item são obrigatórios."
            )

        # Verifica se o item existe
        try:
            Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            raise ValidationError({"item": "Item não encontrado."})

        # Verifica se já existe um chat para essa combinação
        existing_chat = ChatRoom.objects.filter(
            participant_1=participant_1_id, participant_2=participant_2_id, item_id=item_id
        ).first()

        if existing_chat:
            # Se já existir, retorna o chat existente em vez de criar um novo
            serializer = self.get_serializer(existing_chat)
            return Response(serializer.data)

        # Se não existir, cria o chat normalmente
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
