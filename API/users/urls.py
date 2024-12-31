from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    BrandViewSet,
    CategoryViewSet,
    ColorViewSet,
    ItemImageViewSet,
    ItemViewSet,
    TestUserView,
    UserDetailView,
)

router = DefaultRouter()
router.register(r"items", ItemViewSet, basename="item")
router.register(r"categories", CategoryViewSet, basename="category")
router.register(r"colors", ColorViewSet, basename="color")
router.register(r"brands", BrandViewSet, basename="brand")
router.register(r"items/(?P<item_id>[^/.]+)/images", ItemImageViewSet, basename="item-image")

urlpatterns = [
    path("", include(router.urls)),  # Rotas para itens e categorias
    path("auth/user/", UserDetailView.as_view(), name="useer-detail"),
    path("test-user/", TestUserView.as_view(), name="test_user"),
]
