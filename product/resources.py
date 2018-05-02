'''
from import_export import resources
from product.models import ProductCounterSummary

class ProductCounterSummaryResource(resources.ModelResource):
    class Meta:
        model = ProductCounterSummary
'''