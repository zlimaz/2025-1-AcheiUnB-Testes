from rest_framework import serializers
from .models import Brand, Color, Item, Category, ItemImage


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "name", "color_id"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ["id", "name", "brand_id"]


class ItemImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImage
        fields = ["id", "image_url", "item"]
        extra_kwargs = {"item": {"read_only": True}}


class ItemSerializer(serializers.ModelSerializer):
    imagem = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False),
        write_only=True,
        required=False,
    )
    barcode = serializers.CharField(read_only=True)  # Código único do item

    class Meta:
        model = Item
        fields = [
            "id",
            "barcode",
            "name",
            "description",
            "category",
            "location",
            "color",
            "brand",
            "is_valuable",
            "status",
            "found_lost_date",
            "created_at",
            "images",
            "image_url",
        ]

    def create(self, validated_data):
        # Extrai as imagens
        images = validated_data.pop("imagem", [])
        item = super().create(validated_data)

        for image in images:
            upload_result = cloudinary.uploader.upload(image)
            image_url = upload_result.get("secure_url")
            ItemImage.objects.create(item=item, image_url=image_url)

        return item


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "category_id"]
