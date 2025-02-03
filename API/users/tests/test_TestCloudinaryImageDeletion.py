from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase

from users.models import Brand, Category, Color, Item, ItemImage, Location

User = get_user_model()


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
