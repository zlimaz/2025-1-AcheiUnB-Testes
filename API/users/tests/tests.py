from datetime import timedelta
from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.core import mail
from django.core.management import call_command
from django.test import TestCase
from django.utils.timezone import now
from rest_framework.test import APITestCase

from chat.models import ChatRoom
from users.models import Brand, Category, Color, Item, ItemImage, Location

from .match import find_and_notify_matches, hamming_distance


class CleanOldItemsTest(TestCase):
    def setUp(self):
        """
        Configura os dados para os testes:
        - Cria usuários, itens e chats com diferentes datas de criação.
        """
        # Usuários
        self.user1 = User.objects.create_user(username="user1", password="password1")
        self.user2 = User.objects.create_user(username="user2", password="password2")

        # Itens
        self.recent_item = Item.objects.create(
            name="Recent Item",
            user=self.user1,
        )
        self.old_item = Item.objects.create(
            name="Old Item",
            user=self.user2,
        )

        # Atualizar o campo created_at
        self.recent_item.created_at = now() - timedelta(days=10)  # Menos de 2 semanas
        self.recent_item.save()

        self.old_item.created_at = now() - timedelta(days=20)  # Mais de 2 semanas
        self.old_item.save()

        # Chats vinculados aos itens
        self.chat_recent = ChatRoom.objects.create(
            participant_1=self.user1,
            participant_2=self.user2,
            item=self.recent_item,
        )
        self.chat_old = ChatRoom.objects.create(
            participant_1=self.user1,
            participant_2=self.user2,
            item=self.old_item,
        )

    def test_clean_old_items(self):
        """
        Testa se itens com mais de 2 semanas e seus chats vinculados são excluídos.
        """
        # Executa o comando
        call_command("clean_old_items")

        # Verifica se o item antigo foi excluído
        assert not Item.objects.filter(id=self.old_item.id).exists()

        # Verifica se o chat antigo foi excluído automaticamente
        assert not ChatRoom.objects.filter(id=self.chat_old.id).exists()

        # Verifica se o item recente ainda existe
        assert Item.objects.filter(id=self.recent_item.id).exists()

        # Verifica se o chat recente ainda existe
        assert ChatRoom.objects.filter(id=self.chat_recent.id).exists()


User = get_user_model()


class MatchTestCase(TestCase):
    def setUp(self):
        # Criar usuários
        self.user1 = User.objects.create_user(username="user1", password="password")
        self.user2 = User.objects.create_user(username="user2", password="password")

        # Criar categorias
        self.category1 = Category.objects.create(name="Eletrônicos", category_id="01")
        self.category2 = Category.objects.create(name="Roupas", category_id="02")

        # Criar localizações
        self.location1 = Location.objects.create(name="Biblioteca", location_id="01")
        self.location2 = Location.objects.create(name="RU", location_id="02")

        # Criar cores
        self.color1 = Color.objects.create(name="Preto", color_id="01")
        self.color2 = Color.objects.create(name="Azul", color_id="02")

        # Criar marcas
        self.brand1 = Brand.objects.create(name="Samsung", brand_id="01")
        self.brand2 = Brand.objects.create(name="Nike", brand_id="02")

        # Criar itens
        self.item1 = Item.objects.create(
            user=self.user1,
            name="Notebook Perdido",
            category=self.category1,
            location=self.location1,
            color=self.color1,
            brand=self.brand1,
            status="lost",
        )
        self.item2 = Item.objects.create(
            user=self.user2,
            name="Notebook Encontrado",
            category=self.category1,
            location=self.location1,
            color=self.color1,
            brand=self.brand1,
            status="found",
        )
        self.item3 = Item.objects.create(
            user=self.user2,
            name="Celular Encontrado",
            category=self.category1,
            location=self.location2,
            color=self.color2,
            brand=self.brand1,
            status="found",
        )

    def test_basic_match(self):
        matches = find_and_notify_matches(self.item1)
        assert len(matches) == 1  # Apenas um match válido
        assert matches[0].id == self.item2.id

    def test_location_filter(self):
        matches = find_and_notify_matches(self.item1)
        for match in matches:
            assert match.location.id == self.item1.location.id

    def test_category_filter(self):
        item4 = Item.objects.create(
            user=self.user2,
            name="Casaco Encontrado",
            category=self.category2,
            location=self.location1,
            color=self.color1,
            brand=self.brand2,
            status="found",
        )
        matches = find_and_notify_matches(self.item1)
        assert item4 not in matches

    def test_hamming_distance(self):
        # Comparação entre itens similares
        distance = hamming_distance(self.item1.barcode, self.item2.barcode)
        assert distance == 0

        # Comparação entre itens diferentes
        distance = hamming_distance(self.item1.barcode, self.item3.barcode)
        assert distance > 0

    def test_no_matches(self):
        Item.objects.create(
            user=self.user2,
            name="Tablet Encontrado",
            category=self.category1,
            location=self.location2,
            color=self.color2,
            brand=self.brand2,
            status="found",
        )
        matches = find_and_notify_matches(self.item1)
        assert len(matches) == 1  # Apenas item2 é um match válido


class MatchNotificationTestCase(TestCase):
    def setUp(self):
        # Criar usuário com e-mail institucional
        self.user = User.objects.create_user(
            username="user3",
            email="231026714@aluno.unb.br",
            password="password",
        )

        # Criar categorias, localizações, cores e marcas
        self.category = Category.objects.create(name="Eletrônicos", category_id="01")
        self.location = Location.objects.create(name="Biblioteca", location_id="01")
        self.color = Color.objects.create(name="Preto", color_id="01")
        self.brand = Brand.objects.create(name="Samsung", brand_id="01")

        # Criar item perdido
        self.item_lost = Item.objects.create(
            user=self.user,
            name="Relógio de Ouro Perdido",
            category=self.category,
            location=self.location,
            color=self.color,
            brand=self.brand,
            status="lost",
        )

        # Criar item encontrado
        self.item_found = Item.objects.create(
            user=self.user,
            name="Relógio de Ouro Encontrado",
            category=self.category,
            location=self.location,
            color=self.color,
            brand=self.brand,
            status="found",
        )

    def test_notification_email_sent(self):
        # Executar a função de match e notificação
        matches = find_and_notify_matches(self.item_lost)

        # Verificar se o match foi encontrado
        assert len(matches) == 1
        assert matches[0].id == self.item_found.id

        # Verificar se um e-mail foi enviado
        assert len(mail.outbox) == 1
        email = mail.outbox[0]

        # Verificar detalhes do e-mail
        assert (
            email.subject
            == f"Possíveis matches para o seu item perdido: {self.item_lost.name}"
        )
        assert self.item_found.name in email.body
        assert "Biblioteca" in email.body
        assert email.to == [self.user.email]


class APITestItemFilters(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="password")

        # Criar categorias
        self.category1 = Category.objects.create(name="Acessórios", category_id="01")
        self.category2 = Category.objects.create(name="Eletrônicos", category_id="02")

        # Criar cores
        self.color1 = Color.objects.create(name="Preto", color_id="01")
        self.color2 = Color.objects.create(name="Branco", color_id="02")

        # Criar localizações
        self.location1 = Location.objects.create(name="Biblioteca", location_id="01")
        self.location2 = Location.objects.create(name="Sala de Aula", location_id="02")

        # Criar itens
        self.item1 = Item.objects.create(
            user=self.user,
            name="Relógio",
            category=self.category1,
            color=self.color1,
            location=self.location1,  # Atribuir localização
            status="found",
        )
        self.item2 = Item.objects.create(
            user=self.user,
            name="Celular",
            category=self.category2,
            color=self.color2,
            location=self.location2,  # Atribuir localização
            status="lost",
        )

    def test_filter_by_category_name(self):
        response = self.client.get("/api/items/?category_name=Acessórios")
        print("Resposta da API (Categoria):", response.data)
        assert len(response.data["results"]) == 1  # Deve retornar apenas 1 item
        assert response.data["results"][0]["category_name"] == "Acessórios"

    def test_filter_by_color_name(self):
        response = self.client.get("/api/items/?color_name=Preto")
        print("Resposta da API (Cor):", response.data)
        assert len(response.data["results"]) == 1  # Deve retornar apenas 1 item
        assert response.data["results"][0]["color_name"] == "Preto"

    def test_filter_by_status(self):
        response = self.client.get("/api/items/?status=found")
        print("Resposta da API (Status 'found'):", response.data)
        assert len(response.data["results"]) == 1  # Deve retornar apenas 1 item
        assert response.data["results"][0]["status"] == "found"

        response = self.client.get("/api/items/?status=lost")
        print("Resposta da API (Status 'lost'):", response.data)
        assert len(response.data["results"]) == 1  # Deve retornar apenas 1 item
        assert response.data["results"][0]["status"] == "lost"

    def test_filter_by_multiple_parameters(self):
        response = self.client.get("/api/items/?category_name=Acessórios&color_name=Preto")
        print("Resposta da API (Filtros múltiplos):", response.data)
        assert len(response.data["results"]) == 1  # Deve retornar apenas 1 item
        assert response.data["results"][0]["category_name"] == "Acessórios"
        assert response.data["results"][0]["color_name"] == "Preto"

        response = self.client.get("/api/items/?category_name=Acessórios&color_name=Branco")
        print("Resposta da API (Filtros múltiplos sem resultados):", response.data)
        assert len(response.data["results"]) == 0  # Nenhum item deve ser retornado

    def test_no_filters(self):
        response = self.client.get("/api/items/")
        print("Resposta da API (Sem filtros):", response.data)
        assert len(response.data["results"]) == 2  # Todos os itens devem ser retornados

    def test_no_results(self):
        response = self.client.get("/api/items/?category_name=NãoExiste")
        print("Resposta da API (Sem resultados):", response.data)
        assert len(response.data["results"]) == 0  # Nenhum item deve ser retornado

    def test_update_item(self):
        self.client.force_authenticate(user=self.user)
        data = {"name": "Relógio Atualizado"}
        response = self.client.patch(f"/api/items/{self.item1.id}/", data)
        assert response.status_code == 200
        self.item1.refresh_from_db()
        assert self.item1.name == "Relógio Atualizado"

    def test_pagination(self):
        response = self.client.get("/api/items/?page=1")
        assert response.status_code == 200
        assert "results" in response.data
        assert "count" in response.data
        assert "next" in response.data or "previous" in response.data
        assert len(response.data["results"]) <= 10  # Supondo um limite de 10 itens por página

    def test_search_by_name(self):
        response = self.client.get("/api/items/?search=Relógio")
        assert response.status_code == 200
        assert len(response.data["results"]) == 1  # Deve retornar apenas 1 item
        assert response.data["results"][0]["name"] == "Relógio"

    def test_search_by_description(self):
        self.item2.description = "Celular encontrado"
        self.item2.save()

        response = self.client.get("/api/items/?search=Celular")
        assert response.status_code == 200
        assert len(response.data["results"]) >= 1
        assert response.data["results"][0]["description"] == "Celular encontrado"

    def test_search_by_category_name(self):
        response = self.client.get("/api/items/?search=Acessórios")
        assert response.status_code == 200
        assert len(response.data["results"]) == 1
        assert response.data["results"][0]["category_name"] == "Acessórios"

    def test_search_by_location_name(self):
        response = self.client.get("/api/items/?search=Biblioteca")
        assert response.status_code == 200
        assert len(response.data["results"]) >= 1
        assert response.data["results"][0]["location_name"] == "Biblioteca"

    def test_ordering_by_created_at(self):
        response = self.client.get("/api/items/?ordering=created_at")
        assert response.status_code == 200
        results = response.data["results"]
        assert len(results) == 2
        assert results[0]["created_at"] <= results[1]["created_at"]

    def test_ordering_by_found_lost_date(self):
        # Garanta que os itens tenham uma `found_lost_date`
        self.item1.found_lost_date = now() - timedelta(days=1)
        self.item2.found_lost_date = now()
        self.item1.save()
        self.item2.save()

        response = self.client.get("/api/items/?ordering=found_lost_date")
        assert response.status_code == 200
        results = response.data["results"]

        # Ignorar itens sem `found_lost_date`
        results = [r for r in results if r["found_lost_date"] is not None]
        assert len(results) >= 2
        assert results[0]["found_lost_date"] <= results[1]["found_lost_date"]

    def test_reverse_ordering(self):
        response = self.client.get("/api/items/?ordering=-created_at")
        assert response.status_code == 200
        results = response.data["results"]
        assert len(results) == 2
        assert results[0]["created_at"] >= results[1]["created_at"]


class TestCloudinaryImageDeletion(TestCase):
    def setUp(self):
        # Criar usuário
        self.user = User.objects.create_user(username="testuser", password="password")

        # Criar dependências
        self.category = Category.objects.create(name="Acessórios", category_id="01")
        self.location = Location.objects.create(name="Biblioteca", location_id="01")
        self.color = Color.objects.create(name="Preto", color_id="01")
        self.brand = Brand.objects.create(name="Samsung", brand_id="01")

        # Criar item
        self.item = Item.objects.create(
            user=self.user,
            name="Relógio",
            category=self.category,
            location=self.location,
            color=self.color,
            brand=self.brand,
            status="found",
        )

        # Criar imagem vinculada ao item
        self.image = ItemImage.objects.create(
            item=self.item,
            image_url="https://res.cloudinary.com/demo/image/upload/v12345/test_image.jpg",
        )

    @patch("cloudinary.uploader.destroy")
    def test_image_deleted_from_cloudinary(self, mock_destroy):
        # Deletar a imagem e verificar se o Cloudinary foi chamado
        self.image.delete()
        mock_destroy.assert_called_once_with("test_image")  #
