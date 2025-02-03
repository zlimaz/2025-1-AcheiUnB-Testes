from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import TestCase
from users.models import Brand, Category, Color, Item, Location
from users.match import find_and_notify_matches, hamming_distance, get_potential_matches, generate_match_data
from users.tasks import send_match_notification

User = get_user_model()


class MatchTestCase(TestCase):
    def setUp(self):
        # Criar usuários
        self.user1 = User.objects.create_user(username="user1", password="password", email="user1@email.com")
        self.user2 = User.objects.create_user(username="user2", password="password", email="user2@email.com")

        # Criar categorias
        self.category1 = Category.objects.create(name="Eletrônicos", category_id="01")
        self.category2 = Category.objects.create(name="Roupas", category_id="02")  # Diferente para testar

        # Criar localizações
        self.location1 = Location.objects.create(name="Biblioteca", location_id="01")
        self.location2 = Location.objects.create(name="RU", location_id="02")  # Diferente para testar

        # Criar cores
        self.color1 = Color.objects.create(name="Preto", color_id="01")
        self.color2 = Color.objects.create(name="Azul", color_id="02")  # Diferente para testar

        # Criar marcas
        self.brand1 = Brand.objects.create(name="Samsung", brand_id="01")
        self.brand2 = Brand.objects.create(name="Apple", brand_id="02")  # Diferente para testar

        # Criar itens com diferenças nos atributos para gerar `barcodes` distintos
        self.item_lost = Item.objects.create(
            user=self.user1,
            name="Notebook Perdido",
            category=self.category1,
            location=self.location1,
            color=self.color1,
            brand=self.brand1,
            status="lost",
        )
        self.item_found = Item.objects.create(
            user=self.user2,
            name="Notebook Encontrado",
            category=self.category1,  # Mantém a categoria igual
            location=self.location1,  # Mantém a localização igual
            color=self.color1,  # Mantém a cor igual
            brand=self.brand2,  # ALTERA a marca para gerar um barcode diferente
            status="found",
        )

        # Atualiza o banco de dados para garantir que `save()` foi chamado
        self.item_lost.save()
        self.item_found.save()

        print(f"Item Perdido Barcode: {self.item_lost.barcode}")
        print(f"Item Encontrado Barcode: {self.item_found.barcode}")

        self.item_irrelevante = Item.objects.create(
            user=self.user2,
            name="Celular Encontrado",
            barcode="11111111",  # Distância muito alta
            category=self.category1,
            location=self.location2,
            color=self.color2,
            brand=self.brand1,
            status="found",
        )

    def test_hamming_distance(self):
        """Testa se a distância de Hamming é calculada corretamente."""

        # Exibir os barcodes para depuração
        print(f"Barcode Item Perdido: {self.item_lost.barcode}")
        print(f"Barcode Item Encontrado: {self.item_found.barcode}")

        distance = hamming_distance(self.item_lost.barcode, self.item_found.barcode)

        print(f"Distância de Hamming Calculada: {distance}")

        self.assertGreater(distance, 0, f"Esperado > 0, mas recebido {distance}")

    def test_get_potential_matches(self):
        """Testa se os matches potenciais são filtrados corretamente pelo status e distância."""
        matches = get_potential_matches(self.item_lost, opposite_status="found", max_distance=2)
        self.assertIn(self.item_found, matches)  # Item encontrado deve ser um match
        self.assertNotIn(self.item_irrelevante, matches)  # Item irrelevante não pode ser um match

    def test_generate_match_data(self):
        """Testa se os dados estruturados são gerados corretamente."""
        matches = [self.item_found]
        match_data = generate_match_data(matches)

        expected_data = [
            {
                "id": self.item_found.id,
                "name": "Notebook Encontrado",
                "description": self.item_found.description,
                "location": "Biblioteca",
                "found_lost_date": "Data não especificada",
                "image_url": None,  # Sem imagens associadas
            }
        ]

        self.assertEqual(match_data, expected_data)

    @patch("users.tasks.send_match_notification.delay")  # Mock para evitar envio real de email
    def test_find_and_notify_matches(self, mock_send_match_notification):
        """Testa se os matches são encontrados e se a notificação é enviada corretamente."""
        find_and_notify_matches(self.item_lost, max_distance=2)

        # Verifica se o match foi adicionado ao item perdido
        self.item_lost.refresh_from_db()
        self.assertIn(self.item_found, self.item_lost.matches.all())

        # Verifica se a notificação foi disparada corretamente
        mock_send_match_notification.assert_called_once()
        args, kwargs = mock_send_match_notification.call_args
        self.assertEqual(kwargs["to_email"], self.item_lost.user.email)
        self.assertEqual(kwargs["item_name"], self.item_lost.name)
        self.assertTrue(kwargs["matches"])  # Deve conter dados dos matches

    @patch("users.tasks.send_match_notification.delay")
    def test_no_matches(self, mock_send_match_notification):
        """Testa o caso onde nenhum match válido é encontrado."""
        find_and_notify_matches(self.item_irrelevante, max_distance=2)

        # Verifica que nenhum match foi adicionado ao item irrelevante
        self.item_irrelevante.refresh_from_db()
        self.assertEqual(self.item_irrelevante.matches.count(), 0)

        # Verifica que o email não foi enviado
        mock_send_match_notification.assert_not_called()
