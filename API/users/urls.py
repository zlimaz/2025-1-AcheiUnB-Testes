from django.urls import path
from users.views import ItemListCreateView
from .views import UserDetailView

urlpatterns = [
    path("api/items/", ItemListCreateView.as_view(), name="item-list-create"),
    path("auth/user/", UserDetailView.as_view(), name="useer-detail"),
]
