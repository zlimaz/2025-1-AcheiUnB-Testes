
from django.contrib.auth import get_user_model
from django.core import mail
from django.test import TestCase

from users.models import Brand, Category, Color, Item, Location

from users.match import find_and_notify_matches

User = get_user_model()


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

        assert matches is not None, "Erro: `find_and_notify_matches` retornou None, esperado uma lista vazia ou com itens."
        assert isinstance(matches, list), "Erro: `matches` deveria ser uma lista."
        assert len(matches) == 1, f"Erro: esperado 1 match, mas encontrado {len(matches)}"

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
