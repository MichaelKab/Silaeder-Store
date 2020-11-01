import factory

from website.models import Product


class ProductFactory(factory.DjangoModelFactory):
    class Meta:
        model = Product
