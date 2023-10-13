from django.contrib.auth.models import User
from django.db.models import Count, OuterRef, Sum, F
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from catalog.models import Product, ProductAccess
from study.models import LessonStatusEnum, LessonViewInfo
from catalog.serializers import ProductStatisticSerializer


class ProductStatisticViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = ProductStatisticSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)

    def get_queryset(self):
        total_users_count = User.objects.filter(is_active=True).count()
        queryset = Product.objects.all().annotate(
            lesson_view_count=Count(
                LessonViewInfo.objects.filter(
                    lesson__products=OuterRef('id'),
                    status=LessonStatusEnum.VIEWED
                ).values('id')
            ),
            total_view_time=Sum(
                LessonViewInfo.objects.filter(
                    lesson__products=OuterRef('id'),
                ).values('view_time')
            ),
            total_users_on_product=Count(
                ProductAccess.objects.filter(
                    product_id=OuterRef('id')
                ).values('id')
            ),
            purchasing_percent=F('total_users_on_product') / float(total_users_count) * 100
        )
        return queryset
