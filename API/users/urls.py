from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet, CategoryViewSet, ItemImageViewSet, UserDetailView

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='item')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'items/(?P<item_id>[^/.]+)/images', ItemImageViewSet, basename='item-image')

urlpatterns = [
    path("", include(router.urls)),  # Rotas para itens e categorias    
    path("auth/user/", UserDetailView.as_view(), name="useer-detail"),
]
