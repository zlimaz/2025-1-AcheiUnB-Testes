from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.crypto import get_random_string
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Item
from .serializers import ItemSerializer
from msal import ConfidentialClientApplication
from django.shortcuts import redirect
from django.http import JsonResponse
import os
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response


# Configurações do MSAL
CLIENT_ID = os.getenv("MICROSOFT_CLIENT_ID")
CLIENT_SECRET = os.getenv("MICROSOFT_CLIENT_SECRET")
AUTHORITY = os.getenv("AUTHORITY")
REDIRECT_URI = os.getenv("MICROSOFT_REDIRECT_URI")


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
        if user.email and "@aluno.unb.br" in user.email:
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


def microsoft_login(request):
    """Inicia o fluxo de login com Microsoft."""
    app = ConfidentialClientApplication(
        CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
    )
    # URL para redirecionar o usuário para o login da Microsoft
    auth_url = app.get_authorization_request_url(
        scopes=["User.Read"],  # Scopes solicitados
        redirect_uri=REDIRECT_URI,
    )
    return redirect(auth_url)


def microsoft_callback(request):
    """Processa o callback da Microsoft após o login."""
    # Obtém o código de autorização da URL
    code = request.GET.get("code")
    if not code:
        messages.error(request, "Código de autorização não fornecido.")
        return redirect(
            "http://localhost:8000/#/"
        )  # Redireciona para a home se o código não for fornecido

    # Troca o código pelo token
    app = ConfidentialClientApplication(
        CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET
    )
    result = app.acquire_token_by_authorization_code(
        code,
        scopes=["User.Read"],  # Scopes solicitados
        redirect_uri=REDIRECT_URI,
    )

    if "access_token" in result:
        # Você pode usar o token para autenticar o usuário ou armazenar informações adicionais
        user_info = result.get("id_token_claims")

        # (Opcional) Salve as informações do usuário na sessão
        request.session["user"] = {
            "name": user_info.get("name"),
            "email": user_info.get("preferred_username"),
            "oid": user_info.get("oid"),
        }

        # Redireciona para a página inicial
        messages.success(request, "Login realizado com sucesso!")
        return redirect(
            "http://localhost:5173/#/lost"
        )  # Substitua "home" pela URL name da sua página inicial
    else:
        messages.error(request, "Erro ao obter o token de acesso.")
        return redirect(
            "http://localhost:8000/#/"
        )  # Redireciona para a página inicial com erro
