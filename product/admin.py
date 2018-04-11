from django.contrib import admin
from product.models import Product, ProductCounter, ProductCounterSummary

admin.site.register(Product)
admin.site.register(ProductCounter)

@admin.register(ProductCounterSummary)
class ProductCounterSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/sale_summary_change_list.html'
    date_hierarchy = 'created'
    
    def changelist_view(self, request, extra_content=None):
        response = super().changelist_view(
            request,
            extra_content=extra_content,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total': Count('id'),
            'total_product_displayed': Sum('displayed_item'), 
        }

        response.context_data[‘summary’] = list(
            qs
            .distinct()
            .values(‘product’)
            .annotate(**metrics)
            .order_by(‘-total_sales’)
        )
        
        '''
        SELECT DISTINCT user_id, COUNT(*)
            FROM my_model 
            WHERE tag_id = 15 OR tag_id = 17
            GROUP BY user_id 
            HAVING COUNT(*) > 1

        MyModel.objects.filter(row_id__in=[15,17])\
            .distinct()\
            .values('user_id')\
            .annotate(user_count=Count('user_id'))\
            .filter(user_count__gt=1)\
            .order_by('user_id')
        '''