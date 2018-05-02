from django.contrib import admin
from product.models import Product, ProductCounter, ProductCounterSummary
from django.db.models import Count, Sum, Min, Max
from django.db.models.functions import Trunc
from django.db.models import DateTimeField
# from import_export.admin import ImportExportModelAdmin
# from product.resources import ProductCounterSummaryResource


admin.site.register(Product)
admin.site.register(ProductCounter)


def get_next_in_date_hierarchy(request, date_hierarchy):
    if date_hierarchy + '__day' in request.GET:
        return 'hour'
    if date_hierarchy + '__month' in request.GET:
        return 'day'
    if date_hierarchy + '__year' in request.GET:
        return 'week'
    return 'month'

@admin.register(ProductCounterSummary)
class ProductCounterSummaryAdmin(admin.ModelAdmin):
# class ProductCounterSummaryAdmin(ImportExportModelAdmin):
    # resource_class = ProductCounterSummaryResource
    change_list_template = 'admin/productcounter_summary_change_list.html'
    date_hierarchy = 'created'
    # date_hierarchy = get_next_in_date_hierarchy(
    #        self.date_hierarchy)
    list_display = ('product', 'start_datetime', 'end_datetime','displayed_item', 'wasted_item')
    list_display_links = None
    list_filter = ('created', 'product')

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

        # date_hierarchy = get_next_in_date_hierarchy(
        #    request, self.date_hierarchy)

        response.context_data['summary'] = list(
            qs.values('product__name', 'start_datetime', 'end_datetime',
                      'displayed_item', 'wasted_item').annotate(**metrics)
            .order_by('product'))

        response.context_data['summary_total'] = dict(qs.aggregate(**metrics))

        '''
        # Bar Chart
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
        '''

        return response