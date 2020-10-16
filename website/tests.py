from django.test import TestCase

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory
from datetime import datetime
from django.utils import timezone
from website.factories import ProductFactory, SchoolAttendFactory, CustomUserFactory,TransactionUserFactory


class TestCaseForProduct(APITestCase):

    def test_get_product_request_factory(self):
        city = ProductFactory(name_product="Test", description_product="Test", quantity=10)
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCaseForSchoolAttend(APITestCase):

    def test_get_schoolattend_request_factory(self):
        custom_user = CustomUserFactory(password='TESTPASSWORD', username="TEST")
        schoolch = SchoolAttendFactory( id_user_id=custom_user.id, required_days="Test", time_start=9, exception_days="None")
        print(schoolch)
        response = self.client.get("/api/attendance/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCaseForCustomUser(APITestCase):

    def test_get_customuser_request_factory(self):
        custom_user = CustomUserFactory(password='TESTPASSWORD', username="TEST")
        response = self.client.get("/api/user/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestCaseForTransaction(APITestCase):

    def test_get_transaction_request_factory(self):
        custom_user = CustomUserFactory(password='TESTPASSWORD', username="TEST")
        transaction_o = TransactionUserFactory(id_user_id=custom_user.id, description='TEST', cash=0, date=timezone.now())
        response = self.client.get("/api/transaction/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
