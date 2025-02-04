from unittest.mock import patch

from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in
from django.test import TestCase

from users.models import (
    Item,  # Importa o modelo Item corretamente
    ItemImage,
    UserProfile,
)
from users.signals import (
    save_user_profile,
)


class UserProfileSignalTests(TestCase):
    """Testes para os sinais relacionados ao UserProfile."""

    def test_create_user_profile_signal(self):
        """Testa se um UserProfile é criado automaticamente quando um User é criado."""
        user = User.objects.create_user(username="testuser", password="password")

        # Verifica se o perfil foi criado corretamente
        assert UserProfile.objects.filter(user=user).exists()
        assert user.profile is not None

    def test_save_user_profile_signal(self):
        """Testa se o UserProfile é salvo corretamente ao salvar um usuário."""
        user = User.objects.create_user(username="testuser2", password="password")
        user.profile.profile_picture = "http://example.com/image.jpg"
        user.profile.save()

        # Simula a chamada do sinal
        save_user_profile(User, user)
        user.refresh_from_db()

        assert user.profile.profile_picture == "http://example.com/image.jpg"


class WelcomeEmailSignalTests(TestCase):
    """Testes para o envio de e-mail de boas-vindas no primeiro login."""

    @patch("users.tasks.send_welcome_email.delay")  # Mock da função para evitar envio real
    def test_send_welcome_email_on_first_login(self, mock_send_email):
        """Testa se o e-mail de boas-vindas é enviado apenas no primeiro login."""
        user = User.objects.create_user(username="testuser3", password="password")

        # Dispara o sinal manualmente simulando um login
        user_logged_in.send(sender=User, request=None, user=user)

        # Verifica se o e-mail foi enviado
        mock_send_email.assert_called_once_with(user.email, user.first_name)

        # Verifica se o e-mail foi marcado como enviado
        user.profile.refresh_from_db()
        assert user.profile.welcome_email_sent

        # Testa um segundo login - o e-mail NÃO deve ser enviado novamente
        user_logged_in.send(sender=User, request=None, user=user)
        mock_send_email.assert_called_once()  # A chamada deve permanecer a mesma


class CloudinarySignalTests(TestCase):
    """Testes para o sinal de deleção de imagens do Cloudinary."""

    @patch("cloudinary.uploader.destroy")
    def test_delete_image_from_cloudinary(self, mock_cloudinary_destroy):
        """Testa se a imagem é deletada corretamente do Cloudinary."""

        # Criar um Item antes de associar a imagem
        item = Item.objects.create(name="Chave", status="lost")

        # Criar a imagem associada ao Item
        image = ItemImage.objects.create(
            item=item, image_url="http://res.cloudinary.com/demo/image/upload/sample.jpg"
        )

        # Simula a exclusão do objeto
        image.delete()

        # O Cloudinary deve ser chamado para deletar a imagem
        mock_cloudinary_destroy.assert_called_once_with("sample")
