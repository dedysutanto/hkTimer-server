from rest_framework import viewsets
from product.models import Product, ProductCounter
from product.serializers import ProductSerializer, ProductCounterSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCounterViewSet(viewsets.ModelViewSet):
    queryset = ProductCounter.objects.all()
    serializer_class = ProductCounterSerializer