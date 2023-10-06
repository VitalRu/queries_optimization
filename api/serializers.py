from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from lessons.models import Lesson, Product, ProductAccess, ProductLesson, User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fileds = ('title', 'onwer')


class ProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccess
        fields = ('product', 'user')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('title', 'video_link', 'duration', 'products')


class ProductLessonSerializer(serializers.ModelSerializer):
    product_title = serializers.ReadOnlyField(source='product.title')
    lesson_title = serializers.ReadOnlyField(source='lesson.title')

    class Meta:
        model = ProductLesson
        fields = ('product_title', 'lesson_title')
        validators = (
            UniqueTogetherValidator(
                queryset=ProductLesson.objects.all(),
                fields=('product_title', 'lesson_title',)
            ),
        )
