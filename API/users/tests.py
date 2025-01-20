from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase

from .match import find_and_notify_matches, hamming_distance
from .models import Brand, Category, Color, Item, Location

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
        # Limpa o outbox antes de executar o teste
        mail.outbox = []

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
        assert self.item_lost.name in email.body
        assert email.to == [self.user.email]
