import cloudinary.uploader
from django.contrib.auth.models import User
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import ItemImage, UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, "profile"):
        instance.profile.save()


@receiver(post_delete, sender=ItemImage)
def delete_image_from_cloudinary(sender, instance, **kwargs):
    """
    Remove a imagem do Cloudinary quando o ItemImage é deletado.
    """
    if instance.image_url:
        try:
            # Extrair o ID público do Cloudinary da URL
            public_id = instance.image_url.split("/")[-1].split(".")[0]
            cloudinary.uploader.destroy(public_id)
        except Exception as e:
            # Opcional: Adicione logs ou trate o erro de forma adequada
            print(f"Erro ao remover a imagem do Cloudinary: {str(e)}")
