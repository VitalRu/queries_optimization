from rest_framework import viewsets
from lessons.models import Product, Lesson, ProductAccess
from .serializers import ProductSerializer, LessonSerializer


class ProductViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        accessed_products = ProductAccess.objects.filter(
            user=self.request.user
        ).values_list('product', flat=True)
        products = Product.objects.filter(id__in=accessed_products)
        return products.lesson.all()
