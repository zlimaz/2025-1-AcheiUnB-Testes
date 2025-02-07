from unittest.mock import patch

import pytest
from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken

from users.authentication import CookieJWTAuthentication

User = get_user_model()


class CookieJWTAuthenticationTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.authenticator = CookieJWTAuthentication()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass"
        )
        self.token = str(AccessToken.for_user(self.user))

    def test_authenticate_with_cookie(self):
        request = self.factory.get("/")
        request.COOKIES["access_token"] = self.token

        with patch.object(
            CookieJWTAuthentication, "get_validated_token", return_value=self.token
        ):
            with patch.object(CookieJWTAuthentication, "get_user", return_value=self.user):
                user, validated_token = self.authenticator.authenticate(request)

                assert user == self.user
                assert validated_token == self.token

    def test_authenticate_with_header(self):
        request = self.factory.get("/")
        request.META["HTTP_AUTHORIZATION"] = f"Bearer {self.token}"

        with patch.object(
            CookieJWTAuthentication, "get_validated_token", return_value=self.token
        ):
            with patch.object(CookieJWTAuthentication, "get_user", return_value=self.user):
                user, validated_token = self.authenticator.authenticate(request)

                assert user == self.user
                assert validated_token == self.token

    def test_authenticate_without_token(self):
        request = self.factory.get("/")
        assert self.authenticator.authenticate(request) is None

    def test_authenticate_invalid_token(self):
        request = self.factory.get("/")
        request.COOKIES["access_token"] = "invalid.token.value"

        with patch.object(
            CookieJWTAuthentication,
            "get_validated_token",
            side_effect=AuthenticationFailed("Token inválido"),
        ):
            with pytest.raises(AuthenticationFailed):
                self.authenticator.authenticate(request)

    def test_authenticate_with_malformed_header(self):
        request = self.factory.get("/")
        request.META["HTTP_AUTHORIZATION"] = self.token

        with patch.object(
            CookieJWTAuthentication,
            "get_validated_token",
            side_effect=AuthenticationFailed("Token inválido"),
        ):
            with pytest.raises(AuthenticationFailed):
                self.authenticator.authenticate(request)
