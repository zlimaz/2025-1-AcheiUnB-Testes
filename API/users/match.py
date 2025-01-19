from .models import Item
from .utils import send_match_notification


def hamming_distance(barcode1: str, barcode2: str) -> int:
    """calcula a Hamming Distance entre dois barcodes"""
    return sum(c1 != c2 for c1, c2 in zip(barcode1, barcode2))


def find_and_notify_matches(target_item: Item, max_distance=2):
    """encontra possiveis matches para o item fornecido"""

    # Filtrar itens de status oposto a mesma categoria
    from django.db.models import Q

    potential_items = Item.objects.filter(
        ~Q(status=target_item.status),
        category=target_item.category,
        location=target_item.location,
    ).only("id", "barcode", "status", "name", "description", "found_lost_date")

    # Calcular a distancia de Hamming entre os barcodes
    matches = []
    for item in potential_items:
        distance = hamming_distance(target_item.barcode, item.barcode)
        if distance <= max_distance:
            matches.append(item)

    # Notificar os matches
    if matches:
        match_data = [
            {
                "name": match.name,
                "description": match.description,
                "location": (
                    match.location.name if match.location else "Local não especificado"
                ),
                "found_lost_date": match.found_lost_date,
            }
            for match in matches
        ]

        send_match_notification(
            to_email=target_item.user.email,
            item_name=target_item.name,
            matches=match_data,
        )

    return matches
