"""
URL configuration for AcheiUnB project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.shortcuts import render

# View para servir o arquivo Vue.js
def vue_app(request):
    return render(request, 'index.html')  # Caminho para o index.html dentro da pasta templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),  # Rotas do Allauth para login pelo Microsoft
    path('', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('', include('users.urls')),  # Inclui as rotas do app "users"
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obter token de acesso e refresh
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Atualizar token de acesso
    path('api/chat/', include('chat.urls')),
    path('api/', include('users.urls')),  

]