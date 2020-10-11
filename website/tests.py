from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from website.factories import ProductFactory


class TestCaseForCity(APITestCase):

    def test_get_city_request_factory(self):
        city = ProductFactory(name_product="Test", description_product="Test", quantity=10)
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
