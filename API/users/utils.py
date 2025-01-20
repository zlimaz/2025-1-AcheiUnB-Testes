from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_match_notification(to_email, item_name, matches):
    """
    Envia um e-mail notificando o usuário sobre possíveis matches.
    """
    subject = f"Possíveis matches para o seu item perdido: {item_name}"

    # Renderizar o corpo do e-mail usando um template HTML
    html_message = render_to_string(
        "emails/match_notification.html",
        {
            "item_name": item_name,
            "matches": matches,
        },
    )
    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        "acheiunb2024@gmail.com",
        [to_email],
        html_message=html_message,
    )
