import django_filters

from apps.product.models import Product


class ProductFilter(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='iexact')
    stock = django_filters.CharFilter(field_name='stock', lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'category', 'stock']

