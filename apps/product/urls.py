from django.urls import path

from apps.product.views import ProductDetailView, ProductListView, ProductCreateView, ProductImageAddView

urlpatterns = [
    path('product-list/', ProductListView.as_view()),
    path('product-detail/<int:pk>/', ProductDetailView.as_view()),
    path('product-create/', ProductCreateView.as_view()),
    path('<int:pk>/product-image-add/', ProductImageAddView.as_view()),
]
