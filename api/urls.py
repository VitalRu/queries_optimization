from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductLessonsListViewSet, LessonListViewSet


app_name = 'api'

router = DefaultRouter()

router.register(
    'product_lessons', ProductLessonsListViewSet, basename='products_lessons'
)
router.register('lessons', LessonListViewSet, basename='lessons')

urlpatterns = [
    path('', include(router.urls)),
]
