from django.urls import path
from .views import ChatListCreateView, MessageCreateView

urlpatterns = [
    path('chats/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('messages/', MessageCreateView.as_view(), name='message-create'),
]
