from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from website.serializers import *


def main(request):
    html = "<html><body> Страница </body></html>"
    return HttpResponse(html)


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomSerializer(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomSerializer


class SchoolViewSet(ModelViewSet):
    queryset = SchoolAttend.objects.all()
    serializer_class = SchoolAttendSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
