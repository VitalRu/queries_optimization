from django.db.models import F, FilteredRelation, Q
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from catalog.models import ProductAccess
from study.models import Lesson
from study.serializers import MyLessonsSerializer


class MyLessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = MyLessonsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        accesses = ProductAccess.objects.filter(user=self.request.user, is_valid=True)
        queryset = Lesson.objects.filter(
            products=accesses.values('product_id')
        ).alias(
            view_info=FilteredRelation(
                'views',
                condition=Q(user=self.request.user)
            )
        ).annotate(
            status=F('view_info__status'),
            view_info=F('view_info__view_time')
        )
        return queryset
