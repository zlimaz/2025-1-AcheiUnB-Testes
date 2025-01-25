import cloudinary.uploader
from celery import shared_task

from .match import find_and_notify_matches
from .models import Item, ItemImage


@shared_task
def find_and_notify_matches_task(target_item_id, max_distance=2):
    """Task assíncrona para encontrar e notificar matches."""
    try:
        target_item = Item.objects.get(id=target_item_id)
    except Item.DoesNotExist:
        return

    # Chama a lógica de matches
    find_and_notify_matches(target_item, max_distance)


@shared_task
def upload_images_to_cloudinary(item_id, images):
    """Realiza o upload das imagens para o Cloudinary e salva as URLs no banco."""
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return

    for image_content in images:
        try:
            # Fazer o upload para o Cloudinary usando o conteúdo do arquivo
            upload_result = cloudinary.uploader.upload(image_content)
            image_url = upload_result.get("secure_url")

            # Criar a entrada no banco para a imagem
            ItemImage.objects.create(item=item, image_url=image_url)
        except Exception as e:
            # Logar o erro
            print(f"Erro ao fazer upload de imagem para o item {item_id}: {e}")


@shared_task
def remove_images_from_item(image_ids):
    """Remove imagens associadas a um item."""
    try:
        ItemImage.objects.filter(id__in=image_ids).delete()
    except Exception as e:
        print(f"Erro ao remover imagens com IDs {image_ids}: {e}")
