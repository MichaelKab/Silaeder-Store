import factory

from website.models import Product, CustomUser, SchoolAttend, Transaction


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product


class CustomUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = CustomUser


class SchoolAttendFactory(factory.DjangoModelFactory):
    class Meta:
        model = SchoolAttend


class TransactionUserFactory(factory.DjangoModelFactory):
    class Meta:
        model = Transaction
