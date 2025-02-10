from django.test import TestCase
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory

from users.pagination import LostFoundPagination


class LostFoundPaginationTests(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.pagination = LostFoundPagination()

    def test_default_page_size(self):
        django_request = self.factory.get("/")
        request = Request(django_request)
        queryset = list(range(50))

        paginated_qs = self.pagination.paginate_queryset(queryset, request)
        response = self.pagination.get_paginated_response(paginated_qs)

        assert len(paginated_qs) == 27
        assert "count" in response.data
        assert "next" in response.data
        assert "previous" in response.data

    def test_page_size_query_param(self):
        django_request = self.factory.get("/?page_size=10")
        request = Request(django_request)
        queryset = list(range(50))

        paginated_qs = self.pagination.paginate_queryset(queryset, request)
        response = self.pagination.get_paginated_response(paginated_qs)

        assert len(paginated_qs) == 10
        assert "count" in response.data
        assert "next" in response.data
        assert "previous" in response.data
