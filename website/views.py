from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from website.models import Product, UserData
from website.serializers import ProductSerializer


def main(request):
    html = "<html><body> Страница </body></html>"
    return HttpResponse(html)


class ProductsViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
