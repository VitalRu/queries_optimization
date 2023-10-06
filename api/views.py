from django.db.models import Q
from rest_framework import viewsets

from lessons.models import Lesson, Product, ProductAccess

from .serializers import LessonSerializer, ProductSerializer


class ProductLessonsListViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self, *args, **kwargs):
        product_id = self.kwargs.get('product_id')
        user = self.request.user
        queryset = Lesson.objects.filter(
            Q(lesson_products__product_id=product_id)
            & Q(lesson_products__product__user=user)
        )
        return queryset


class LessonListViewSet(viewsets.ModelViewSet):
    serializer_class = LessonSerializer

    def get_queryset(self):
        accessed_products = ProductAccess.objects.filter(
            user=self.request.user
        ).values_list('product', flat=True)
        products = Product.objects.filter(id__in=accessed_products)
        querysets = []
        for product in products:
            querysets.append(product.lesson.all())
        union_queryset = querysets[0].union(*querysets[1:])
        return union_queryset


class ProductInfoViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
