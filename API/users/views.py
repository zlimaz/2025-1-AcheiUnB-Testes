from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from allauth.socialaccount.models import SocialAccount
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


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

    def ItemListCreateView(ListCreateAPIView):
        queryset = Item.objects.all()
        serializer_class = ItemSerializer
        permission_classes = [IsAuthenticatedOrReadOnly]


class UserDetailView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retorna os dados do usuário autenticado",
        responses={
            200: openapi.Response(
                description="Usuário autenticado",
                examples={
                    "application/json": {
                        "id": 2,
                        "username": "testuser",
                        "email": "231026714@aluno.unb.br",
                        "first_name": "Euller",
                        "last_name": "Silva",
                        "matricula": "231026714",
                        "foto": "https://foto.unb.br/user-picture.jpg",
                    }
                },
            )
        },
    )

    def get(self, request):
        user = request.user
        social_account = SocialAccount.objects.filter(
            user=user, provider="microsoft"
        ).first()

        # Extrai a matrícula e a foto do usuário(se disponivel)
        if user.email and '@aluno.unb.br' in user.email:
            matricula = user.email.split("@")[0]
        else:
            matricula = None

        foto = social_account.extra_data.get("photo", None) if social_account else None

        user_data = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "matricula": matricula,
            "foto": foto,
        }
        return Response(user_data)
