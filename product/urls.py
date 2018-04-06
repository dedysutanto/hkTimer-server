from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet

router = DefaultRouter(trailing_slash=False)
router.register(prefix='product', viewset=ProductViewSet)

urlpatterns = router.urls