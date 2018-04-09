from rest_framework import serializers
from product.models import Product, ProductCounter


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'img', 'duration', 'limit', 'isWarning',
                  'isTimerRunning', 'isClicked', 'start_time', 'end_time',
                  'displayed_item', 'wasted_item')


class ProductCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCounter
        fields = ('id', 'uuid', 'product', 'start_time', 'end_time',
                  'displayed_item', 'wasted_item')
