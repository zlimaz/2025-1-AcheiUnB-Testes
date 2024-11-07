from django.shortcuts import render
from django.contrib.auth import login
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string

# Create your views here.
def anon_login(request):
    username = get_random_string(length=10)
    user = User.objects.create_user(username=username)
    login(request, user)
    messages.success(request, "Você entrou anonimamente.")
    return redirect('/')
