from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class UserDetailTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            email="231026714@aluno.unb.br",
            password="password123",
            first_name="Euller",
            last_name="Silva",
        )
        self.token = Token.objects.create(user=self.user)

    def test_authenticated_user_details(self):
        sucess = 200
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get("/api/auth/user/")
        assert response.status_code == sucess
        assert response.data["username"] == "testuser"
        assert response.data["matricula"] == "231026714"
        assert response.data["email"] == "231026714@aluno.unb.br"
