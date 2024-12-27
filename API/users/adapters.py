from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialApp

class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_app(self, request, provider, client_id=None):
        apps = SocialApp.objects.filter(provider=provider)
        if client_id:
            apps = apps.filter(client_id=client_id)
        if apps.exists():
            return apps.first()  # Garante que a primeira entrada válida seja usada
        raise SocialApp.DoesNotExist("Nenhuma configuração de aplicativo encontrada para o provedor")
    