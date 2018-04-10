from rest_framework import serializers
from product.models import Product, ProductCounter


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('id', 'name', 'img', 'duration', 'limit', 'isWarning',
        #          'isTimerRunning', 'isClicked', 'start_time', 'end_time',
        #          'displayed_item', 'wasted_item', 'left_time')


class ProductCounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCounter
        fields = '__all__'
        # fields = ('id', 'uuid', 'product_id', 'start_time', 'end_time',
        #          'displayed_item', 'wasted_item')
