from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from users.pagination import LostFoundPagination


class LostFoundPaginationTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.pagination = LostFoundPagination()

    def test_default_page_size(self):
        """Testa se a paginação retorna o número correto de itens por página."""
        django_request = self.factory.get("/")
        request = Request(django_request)  # Converte para DRF Request
        queryset = list(range(50))  # Simula um queryset com 50 itens

        paginated_qs = self.pagination.paginate_queryset(queryset, request)
        response = self.pagination.get_paginated_response(paginated_qs)

        assert len(paginated_qs) == 27  # O padrão definido é 27 itens
        assert "count" in response.data  # Verifica se os metadados existem
        assert "next" in response.data  # Verifica se o link 'next' existe
        assert "previous" in response.data  # Verifica se o link 'previous' existe

    def test_page_size_query_param(self):
        """Testa se a paginação respeita o parâmetro page_size."""
        django_request = self.factory.get(
            "/?page_size=10"
        )  # Define um tamanho de página menor
        request = Request(django_request)  # Converte para DRF Request
        queryset = list(range(50))

        paginated_qs = self.pagination.paginate_queryset(queryset, request)
        response = self.pagination.get_paginated_response(paginated_qs)

        assert len(paginated_qs) == 10  # Deve limitar a 10 itens conforme o parâmetro
        assert "count" in response.data
        assert "next" in response.data
        assert "previous" in response.data
