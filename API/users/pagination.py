from rest_framework.pagination import PageNumberPagination


class LostFoundPagination(PageNumberPagination):
    page_size = 27  # Ajuste para exibir 20 itens por página
    page_size_query_param = "page_size"  # Permite ajustar dinamicamente o tamanho da página
