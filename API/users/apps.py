# API/chat/apps.py

from django.apps import AppConfig


class ChatConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "API.chat"  # <--- REVERTIDO PARA ESTE NOME

    def ready(self):
        # Usar importação relativa para consistência
        from . import signals