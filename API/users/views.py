from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Item
from .serializers import ItemSerializer


class ItemListCreateView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filtrar itens por categoria se passado na query string
        category = self.request.query_params.get("category")
        is_valuable = self.request.query_params.get("is_valuable")

        queryset = super().get_queryset()
        if category:
            queryset = queryset.filter(category=category)
        if is_valuable is not None:
            queryset = queryset.filter(is_valuable=is_valuable.lower() == "true")

        return queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user if self.request.user.is_authenticated else None
        )


# Create your views here.


def anon_login(request):
    username = get_random_string(length=10)
    user = User.objects.create_user(username=username)
    login(request, user)
    messages.success(request, "Você entrou anonimamente.")
    return redirect("/")
