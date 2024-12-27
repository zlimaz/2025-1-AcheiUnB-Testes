from rest_framework import serializers
from .models import Item, Category, ItemImage


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id', 'image_url', 'item']
        extra_kwargs = {'item': {'read_only': True}}


class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)  # Relacionamento com imagens

    class Meta:
        model = Item
        fields = [
            'id',
            'name',
            'description',
            'category',
            'location',
            'color',
            'is_valuable',
            'status',
            'found_lost_date',
            'created_at',
            'images',
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'category_id']
