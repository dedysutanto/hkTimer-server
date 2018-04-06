from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, ProductCounterViewSet

router = DefaultRouter(trailing_slash=False)
router.register(prefix='product', viewset=ProductViewSet)
router.register(prefix='productcounter', viewset=ProductCounterViewSet)

urlpatterns = router.urls