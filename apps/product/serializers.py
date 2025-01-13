from rest_framework import serializers

from .models import Product


class BaseProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.SerializerMethodField()

    def get_discounted_price(self, instance):
        if instance.discount is not None:
            discounted_price = instance.price - (instance.price * instance.discount / 100)
            return discounted_price
        return None


class ProductListSerializer(BaseProductSerializer):
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['title', 'price', 'stock', 'discounted_price']
    

class ProductDetailSerializer(BaseProductSerializer):
    discounted_price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'
