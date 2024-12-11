from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


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
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)
        response = self.client.get("/api/auth/user/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "testuser")
        self.assertEqual(response.data["matricula"], "231026714")
        self.assertEqual(response.data["email"], "231026714@aluno.unb.br")
