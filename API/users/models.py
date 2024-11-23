from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('achado', 'Achado'),
        ('perdido', 'Perdido'),
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # Quem registrou o item
    name = models.CharField(max_length=100)  # Nome do item
    description = models.TextField(blank=True)  # Descrição opcional
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)  # Achado ou Perdido
    location = models.CharField(max_length=100)  # Local onde foi encontrado
    image = models.ImageField(upload_to='items/', blank=True, null=True)  # Imagem opcional
    is_valuable = models.BooleanField(default=False)  # Indica se o item é valioso
    created_at = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return self.name
