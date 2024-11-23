from django.urls import path
from users.views import ItemListCreateView

urlpatterns = [
    path('api/items/', ItemListCreateView.as_view(), name='item-list-create'),
]
