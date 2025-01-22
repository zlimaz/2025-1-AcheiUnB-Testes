from rest_framework_simplejwt.authentication import JWTAuthentication


class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):

        raw_token = request.COOKIES.get("access_token")

        if not raw_token:
            raw_token = request.META.get("HTTP_AUTHORIZATION")
            if raw_token:
                if raw_token.startswith("Bearer "):
                    raw_token = raw_token[7:]

        if not raw_token:
            return None

        # Obtém o token validado
        validated_token = self.get_validated_token(raw_token)
        user = self.get_user(validated_token)

        return user, validated_token