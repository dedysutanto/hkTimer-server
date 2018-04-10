from django.contrib import admin
from product.models import Product, ProductCounter

admin.site.register(Product)
admin.site.register(ProductCounter)