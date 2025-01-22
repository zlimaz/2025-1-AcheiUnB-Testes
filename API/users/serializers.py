import cloudinary.uploader
from rest_framework import serializers

from .models import Brand, Category, Color, Item, ItemImage, Location

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name", "category_id"]

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ["id", "name", "location_id"]


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
    images = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False),
        write_only=True,
        required=False,
    )
    image_urls = serializers.SerializerMethodField(read_only=True)
    barcode = serializers.CharField(read_only=True)  # Código único do item
    category_name = serializers.SerializerMethodField()
    location_name = serializers.SerializerMethodField()
    color_name = serializers.SerializerMethodField()
    brand_name = serializers.SerializerMethodField()
    location = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), required=False
    )

    class Meta:
        model = Item
        fields = [
            "id",
            "barcode",
            "name",
            "description",
            "category",
            "category_name",
            "location",
            "location_name",
            "color",
            "color_name",
            "brand",
            "brand_name",
            "status",
            "found_lost_date",
            "created_at",
            "images",  # Para retornar imagens associadas ao item
            "image_urls",  # Para fazer upload de imagens
        ]

    def create(self, validated_data):
        # Extrai as imagens
        images = validated_data.pop("images", [])
        MAX_IMAGES = 3

        if len(images) > MAX_IMAGES:
            raise serializers.ValidationError("Você pode adicionar no máximo 3 imagens.")
        item = super().create(validated_data)

        for image in images:
            if item.images.count() >= MAX_IMAGES:
                raise serializers.ValidationError(
                    "O item já possui o número máximo de 3 imagens."
                )
            try:
                upload_result = cloudinary.uploader.upload(image)
                image_url = upload_result.get("secure_url")
                ItemImage.objects.create(item=item, image_url=image_url)
            except Exception as e:
                raise serializers.ValidationError({"images": str(e)})

        return item
    def get_category_name(self, obj):
        return obj.category.name if obj.category else None
    
    def get_location_name(self, obj):
        return obj.location.name if obj.location else None
    
    def get_color_name(self, obj):
        return obj.color.name if obj.color else None
    
    def get_brand_name(self, obj):
        return obj.brand.name if obj.brand else None
    
    def get_image_urls(self, obj):
        return [image.image_url for image in obj.images.all()]
        


