from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.crypto import get_random_string
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from .models import Brand, Color, Item
from .serializers import BrandSerializer, ColorSerializer, ItemSerializer
from msal import ConfidentialClientApplication
from django.shortcuts import redirect
from django.http import JsonResponse
import os
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Item, Category
from .serializers import ItemSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import status
from .serializers import ItemImageSerializer
from .models import Item, ItemImage


# Configurações do MSAL
CLIENT_ID = os.getenv("MICROSOFT_CLIENT_ID")
CLIENT_SECRET = os.getenv("MICROSOFT_CLIENT_SECRET")
AUTHORITY = os.getenv("AUTHORITY")
REDIRECT_URI = os.getenv("MICROSOFT_REDIRECT_URI")


class ItemViewSet(ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'color', 'brand', 'is_valuable', 'status']
    search_fields = ['name', 'location', 'description']
    ordering_fields = ['created_at', 'found_lost_date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user if self.request.user.is_authenticated else None)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ColorViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
class ItemImageViewSet(ModelViewSet):
    serializer_class = ItemImageSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        item_id = self.kwargs.get("item_id")
        return ItemImage.objects.filter(item_id=item_id)

    def create(self, request, *args, **kwargs):
        item_id = self.kwargs.get("item_id")
        try:
            item = Item.objects.get(id=item_id)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(item=item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
            "http://localhost:8000/#/found"
        )  # Substitua "home" pela URL name da sua página inicial
    else:
        messages.error(request, "Erro ao obter o token de acesso.")
        return redirect(
            "http://localhost:8000/#/"
        )  # Redireciona para a página inicial com erro
