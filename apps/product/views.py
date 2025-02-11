from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.db.models import Avg

from apps.generals.permissions import IsOwner, IsProductOwner
from apps.generals.filters import ProductFilter

from apps.product.models import Product, ProductImage
from apps.product.serializers import ProductDetailSerializer, ProductListSerializer, ProductCreateSerializer, ProductImageSerializer


class StandartResultPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page'


@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related('reviews').annotate(avg_rating=Avg('reviews__rating'))
    serializer_class = ProductListSerializer
    # pagination_class = StandartResultPagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = ProductFilter
    search_fields = ['title', ]
    permission_classes = [permissions.IsAuthenticated,]


@method_decorator(cache_page(60 * 5), name='dispatch')
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductImageAddView(generics.CreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    permission_classes = [IsProductOwner, ]

    
        