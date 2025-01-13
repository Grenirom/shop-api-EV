from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination

from apps.product.models import Product
from apps.product.serializers import ProductDetailSerializer, ProductListSerializer

class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    pagination_class = StandartResultPagination
    permission_classes = [permissions.IsAuthenticated,]


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
