from django.urls import include, path
from rest_framework.routers import SimpleRouter

from study.views import MyLessonsByProductViewSet, MyLessonsViewSet


router = SimpleRouter()

router.register('my-lessons', MyLessonsViewSet, 'my-lessons')

urlpatterns = [
    path('by-product/<int:product_id>/lessons/', MyLessonsByProductViewSet.as_view({'get': 'list'})),
    path('', include(router.urls))
]
