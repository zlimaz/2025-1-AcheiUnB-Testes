from celery import shared_task

from .match import find_and_notify_matches
from .models import Item


@shared_task
def find_and_notify_matches_task(target_item_id, max_distance=2):
    """Task assíncrona para encontrar e notificar matches."""
    try:
        target_item = Item.objects.get(id=target_item_id)
    except Item.DoesNotExist:
        return

    # Chama a lógica de matches
    find_and_notify_matches(target_item, max_distance)
