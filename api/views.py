from rest_framework import viewsets
from lessons.models import Product
from .serializers import ProductSerializer


class ProductListViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
