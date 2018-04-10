from django.contrib import admin
from product.models import Product, ProductCounter, ProductCounterSummary

admin.site.register(Product)
admin.site.register(ProductCounter)

@admin.register(ProductCounterSummary)
class ProductCounterSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'created'
