from rest_framework.routers import DefaultRouter
from website.views import ProductsViewSet

router = DefaultRouter(trailing_slash=True)

router.register('products', ProductsViewSet)
