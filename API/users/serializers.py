from rest_framework import serializers
from .models import Brand, Color, Item, Category, ItemImage

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id', 'name', 'color_id']
    
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'brand_id']

class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ['id', 'image_url', 'item']
        extra_kwargs = {'item': {'read_only': True}}


class ItemSerializer(serializers.ModelSerializer):
    images = ItemImageSerializer(many=True, read_only=True)  # Relacionamento com imagens
    barcode = serializers.CharField(read_only=True)  # Código único do item

    class Meta:
        model = Item
        fields = [
            'id',
            'barcode',
            'name',
            'description',
            'category',
            'location',
            'color',
            'brand',
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
