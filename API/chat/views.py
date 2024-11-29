from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

class ChatListCreateView(APIView):
    def get(self, request):
        chats = Chat.objects.filter(participants=request.user)
        serializer = ChatSerializer(chats, many=True)
        return Response(serializer.data)

    def post(self, request):
        participants = request.data.get('participants', [])
        chat, created = Chat.objects.get_or_create(participants__id__in=participants)
        if created:
            chat.participants.add(*participants)
        serializer = ChatSerializer(chat)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class MessageCreateView(APIView):
    def post(self, request):
        data = request.data
        data['sender'] = request.user.id
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
