from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users import views
from users.views import DeleteUserView, microsoft_callback


def vue_app(request):
    return render(request, "index.html")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("microsoft/login/", views.microsoft_login, name="microsoft_login"),
    path("microsoft/callback/", views.microsoft_callback, name="microsoft_callback"),
    path(
        "accounts/microsoft/login/callback/",
        microsoft_callback,
        name="microsoft_callback",
    ),
    path("", vue_app, name="vue_home"),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/chat/", include("chat.urls")),
    path("api/", include("users.urls")),
    path("delete-user/<int:user_id>/", DeleteUserView.as_view(), name="delete_user"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
