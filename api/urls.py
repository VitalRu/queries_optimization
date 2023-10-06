from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, LessonViewSet


app_name = 'api'

router = DefaultRouter()

router.register('products', ProductViewSet, basename='products')
router.register('lessons', LessonViewSet, basename='lessons')

urlpatterns = [
    path('', include(router.urls)),
]
