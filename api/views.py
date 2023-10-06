from rest_framework import viewsets
from lessons.models import Product, ProductAccess
from .serializers import ProductSerializer, LessonSerializer


class ProductLessonsListViewSet(viewsets.ViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class LessonListViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        accessed_products = ProductAccess.objects.filter(
            user=self.request.user
        ).values_list('product', flat=True)
        products = Product.objects.filter(id__in=accessed_products)
        querysets = []
        for product in products:
            querysets.append(product.lessons.all())
        union_queryset = querysets[0].union(*querysets[1:])
        return union_queryset
