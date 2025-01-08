from django.urls import path

from .views import RegisterView, ActivateView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('activate/', ActivateView.as_view()),
]