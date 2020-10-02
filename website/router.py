from rest_framework.routers import DefaultRouter
from website.views import *

router = DefaultRouter(trailing_slash=True)

router.register('products', ProductsViewSet)
router.register('user', CustomSerializer)
router.register('attendance', SchoolViewSet)
router.register('transaction', TransactionViewSet)
