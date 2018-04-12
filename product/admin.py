from django.contrib import admin
from product.models import Product, ProductCounter, ProductCounterSummary
from django.db.models import Count, Sum, Min, Max
from django.db.models.functions import Trunc
from django.db.models import DateTimeField


admin.site.register(Product)
admin.site.register(ProductCounter)


@admin.register(ProductCounterSummary)
class ProductCounterSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/productcounter_summary_change_list.html'
    # Grappelli specific
    change_list_template = 'admin/change_list_filter_sidebar.html'
    # change_list_template = 'product/productcounter_summary_change_list.html'
    # change_list_template = 'admin/change_list.html'
    change_list_filter_template = 'admin/filter_listing.html'
    # End - Grappelli
    date_hierarchy = 'created'
    list_display = ('product', 'start_datetime', 'end_datetime','displayed_item', 'wasted_item')
    list_display_links = None
    list_filter = ('product', )

    def changelist_view(self, request):
        response = super().changelist_view(request)

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'product_count': Count('product'),
            'displayed_sum': Sum('displayed_item'),
            'wasted_sum': Sum('wasted_item'),
        }

        response.context_data['summary'] = list(
            qs.values('product__name', 'start_datetime', 'end_datetime',
                      'displayed_item', 'wasted_item').annotate(**metrics)
            .order_by('product'))

        response.context_data['summary_total'] = dict(qs.aggregate(**metrics))

        summary_over_time = qs.annotate(
            period=Trunc(
                'created',
                'day',
                output_field=DateTimeField(),
            ),
        ).values('period').annotate(total=Sum('sold_item')).order_by('period')
        
        summary_range = summary_over_time.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = summary_range.get('high', 0)
        low = summary_range.get('low', 0)

        response.context_data['summary_over_time'] = [{
            'period': x['period'],
            'total': x['total'] or 0,
            'pct': \
               ((x['total'] or 0) - low) / (high - low) * 100 
               if high > low else 0,
        } for x in summary_over_time]

        return response