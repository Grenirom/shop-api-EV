from django.urls import path

from apps.product.views import ProductDetailView, ProductListView

urlpatterns = [
    path('product-list/', ProductListView.as_view()),
    path('product-detail/<int:pk>/', ProductDetailView.as_view())
]
