from rest_framework import viewsets
from django.views import generic
from django.shortcuts import render
from django.db.models import Sum, Count
from product.models import Product, ProductCounter
from product.serializers import ProductSerializer, ProductCounterSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCounterViewSet(viewsets.ModelViewSet):
    queryset = ProductCounter.objects.all()
    serializer_class = ProductCounterSerializer


def getProductCounterSummary(request):
    # ProductCounter.objects.filter()
    # .distinct().values('product')
    # .annotate(product_count=Count('product'),
    # displayed_sum=Sum('displayed_item'),
    # wasted_sum=Sum('wasted_item'))
    # .order_by('product')
    template_name = 'product/productcounter_summary.html'
    qs = ProductCounter.objects.filter().distinct().values('product', 'product__name', 'product__id').annotate(
        product_count=Count('product'),
        displayed_sum=Sum('displayed_item'),
        wasted_sum=Sum('wasted_item')).order_by('product')

    return render(request, template_name, { 'objects': qs })

def getProductCounterAll(request):
    template_name = 'product/productcounter_all.html'
    qs = ProductCounter.objects.filter()
    print(qs)
    return render(request, template_name, { 'objects': qs })
