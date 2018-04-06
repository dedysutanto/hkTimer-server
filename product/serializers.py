from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'img', 'duration', 'start_time', 'end_time',
                  'click_count', 'display', 'wasted', 'limit', 'isWarning',
                  'isTimerRunning')
