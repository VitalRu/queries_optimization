from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from catalog.models import ProductAccess
from study.models import Lesson


class MyLessonsViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    serializer_class = None
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        accesses = ProductAccess.objects.filter(user=self.request.user, is_valid=True)
        queryset = Lesson.objects.filter(products=accesses.values('product_id'))
