from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('proadmin/', admin.site.urls),
    path('', include('product.urls')),
]
