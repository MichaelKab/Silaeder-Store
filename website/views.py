from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from website.serializers import ProductSerializer, CustomSerializer, SchoolAttendSerializer, TransactionSerializer
from website.models import Product, CustomUser, SchoolAttend, Transaction


def main(request):
    html = "<html><body> Страница{}</body></html>"
    return HttpResponse(html)


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerializer


class SchoolViewSet(ModelViewSet):
    queryset = SchoolAttend.objects.all()
    serializer_class = SchoolAttendSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
