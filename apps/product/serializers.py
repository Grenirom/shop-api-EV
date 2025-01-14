from rest_framework import serializers

from .models import Product, ProductImage


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
        fields = ['id', 'title', 'price', 'stock', 'discounted_price']
    

class ProductDetailSerializer(BaseProductSerializer):
    discounted_price = serializers.SerializerMethodField()
    owner = serializers.ReadOnlyField(source='owner.email')
    product_images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_product_images(self, instance):
        product_images = instance.images.all()
        if product_images:
            return ProductImageSerializer(product_images, many=True).data
        return None
    

class ProductCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'title',
            'price',
            'description',
            'quantity',
            'discount',
            'category',
        ]


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'
        

