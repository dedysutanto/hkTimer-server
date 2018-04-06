from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('proadmin/', admin.site.urls),
    path('', include('product.urls')),
]
