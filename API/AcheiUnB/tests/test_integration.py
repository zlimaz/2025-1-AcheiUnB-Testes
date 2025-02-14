import pytest
from unittest.mock import patch
import requests
from django.contrib.auth import get_user_model
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()

def get_jwt_token(user):
    token = str(AccessToken.for_user(user))
    return token

@pytest.fixture
def mock_authentication():
    user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass")
    token = get_jwt_token(user)
    
    with patch("users.authentication.CookieJWTAuthentication.authenticate") as mock_auth:
        mock_auth.return_value = (user, token)
        yield mock_auth

@pytest.mark.django_db
def test_create_item(mock_authentication):
    item_data = {
        "barcode": "01010102",
        "name": "testeEditar",
        "user_id": 1,
        "description": "Descrição do item aqui",
        "category": 1,
        "category_name": "Calçado",
        "location": 1,
        "location_name": "Biblioteca",
        "color": 1,
        "color_name": "Rosa",
        "brand": 1,
        "brand_name": "Stanley",
        "status": "found",
        "found_lost_date": "2025-01-19T15:49:28.598322-03:00",
    }
    
    response = requests.post("http://localhost:8000/api/items/", json=item_data, cookies={"access_token": mock_authentication.return_value[1]})
    
    assert response.status_code == 201 
    assert "id" in response.json()

@pytest.mark.django_db
def test_list_items(mock_authentication):
    response = requests.get("http://localhost:8000/api/items/", cookies={"access_token": mock_authentication.return_value[1]})
    
    assert response.status_code == 200
    assert "results" in response.json()

@pytest.mark.django_db
def test_filter_items(mock_authentication):
    params = {
        "location_name": "Biblioteca",
        "category_name": "Calçado",
    }
    
    response = requests.get("http://localhost:8000/api/items/", cookies={"access_token": mock_authentication.return_value[1]}, params=params)
    
    assert response.status_code == 200
    assert len(response.json()['results']) > 0 

@pytest.mark.django_db
def test_search_items(mock_authentication):
    params = {"search": "teste"}
    
    response = requests.get("http://localhost:8000/api/items/", cookies={"access_token": mock_authentication.return_value[1]}, params=params)
    
    assert response.status_code == 200
    assert len(response.json()['results']) > 0 