from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Nome da categoria
    category_id = models.CharField(max_length=10, unique=True)  # ID único da categoria

    def __str__(self):
        return self.name


class Item(models.Model):
    STATUS_CHOICES = [
        ("found", "Achado"),
        ("lost", "Perdido"),
    ]

    COLOR_CHOICES = [
        ("Red", "Vermelho"),
        ("Blue", "Azul"),
        ("Green", "Verde"),
        ("Black", "Preto"),
        ("White", "Branco"),
        ("Other", "Outro"),
    ]

    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )  # Quem registrou o item
    name = models.CharField(max_length=100)  # Nome do item
    description = models.TextField(max_length=500, blank=True)  # Descrição opcional
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True
    )  # Categoria do item
    location = models.CharField(max_length=100)  # Local onde foi encontrado ou perdido
    color = models.CharField(
        max_length=10, choices=COLOR_CHOICES, blank=True
    )  # Cor do item (opcional)
    is_valuable = models.BooleanField(default=False)  # Indica se o item é valioso
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default="lost"
    )  # Diferencia entre Achado ou Perdido
    found_lost_date = models.DateTimeField(null=True, blank=True)  # Data personalizada
    created_at = models.DateTimeField(auto_now_add=True)  # Data de cadastro automático

    def __str__(self):
        return self.name


class ItemImage(models.Model):
    item = models.ForeignKey(Item, related_name="images", on_delete=models.CASCADE)
    image_url = models.URLField()  # URL para armazenar imagens remotamente

    def __str__(self):
        return f"Image for {self.item.name}"
