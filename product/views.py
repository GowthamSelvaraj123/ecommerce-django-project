from rest_framework.generics import ListAPIView
from .models import Product
from .serializers import ProductSerializer
from django.http import HttpResponse
import logging

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

logger = logging.getLogger('django')

def test_log(request):
    logger.debug("Test log message hit")
    return HttpResponse("Log message sent")