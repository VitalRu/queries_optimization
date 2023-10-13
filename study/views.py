from django.db.models import F, FilteredRelation, Q
from rest_framework import exceptions, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from catalog.models import ProductAccess
from study.models import Lesson
from study.serializers import MyLessonsSerializer


def get_product_accesses(user):
    return ProductAccess.objects.filter(user=user, is_valid=True)


class MyLessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyLessonsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        accesses = get_product_accesses(self.request.user)
        queryset = Lesson.objects.filter(
            products__in=accesses.values('product_id')
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__view_time')
        )
        return queryset


class MyLessonsByProductViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = None
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        accesses = get_product_accesses(self.request.user)
        product_id = self.kwargs['product_id']

        if product_id in accesses.values_list('product_id', flat=True):
            raise exceptions.NotFound

        queryset = Lesson.objects.filter(
            products=product_id
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(views__user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_time=F('view_info__view_time'),
            last_view_datetime=F('view_info__last_view_datetime')
        )
        return queryset
