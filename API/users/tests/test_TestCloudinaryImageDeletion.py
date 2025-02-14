from unittest.mock import patch

from django.contrib.auth import get_user_model
from django.test import TestCase

from users.models import Brand, Category, Color, Item, ItemImage, Location

User = get_user_model()


class TestCloudinaryImageDeletion(TestCase):
    def setUp(self):
        Brand.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
        Color.objects.all().delete()
        Item.objects.all().delete()
        ItemImage.objects.all().delete()

        self.user = User.objects.create_user(username="testuser", password="password")

        self.category = Category.objects.create(name="Acessórios", category_id="01")
        self.location = Location.objects.create(name="Biblioteca", location_id="01")
        self.color = Color.objects.create(name="Preto", color_id="01")
        self.brand = Brand.objects.create(name="Samsung", brand_id="01")

        self.item = Item.objects.create(
            user=self.user,
            name="Relógio",
            category=self.category,
            location=self.location,
            color=self.color,
            brand=self.brand,
            status="found",
        )

        self.image = ItemImage.objects.create(
            item=self.item,
            image_url="https://res.cloudinary.com/demo/image/upload/v12345/test_image.jpg",
        )

    @patch("cloudinary.uploader.destroy")
    def test_image_deleted_from_cloudinary(self, mock_destroy):
        self.image.delete()
        mock_destroy.assert_called_once_with("test_image")  #
