from django.urls import path
from .views import ProductListAPIView, test_log

urlpatterns = [
    path('', ProductListAPIView.as_view(), name='product-list'),
    path('log-test/', test_log),
]