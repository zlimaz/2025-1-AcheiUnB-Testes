from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ChatRoomViewSet, ClearChatsView, MessageViewSet

router = DefaultRouter()
router.register(r"chatrooms", ChatRoomViewSet, basename="chatroom")
router.register(r"messages", MessageViewSet, basename="message")

urlpatterns = [
    path("", include(router.urls)),
    path("clear_chats/", ClearChatsView.as_view(), name="clear_chats"),
]
