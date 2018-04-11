from django.urls import path
from rest_framework.routers import DefaultRouter
from product.views import ProductViewSet, ProductCounterViewSet
from product.views import getProductCounterSummary, getProductCounterAll
from django.contrib import admin


router = DefaultRouter(trailing_slash=False)
router.register(prefix='product', viewset=ProductViewSet)
router.register(prefix='productcounter', viewset=ProductCounterViewSet)

admin.site.site_header = 'Hokben Timer'
urlpatterns = router.urls
# urlpatterns += [
#    path('productcountersummary', getProductCounterSummary),
#    path('productcounterall', getProductCounterAll),
# ]