from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from datetime import timedelta

from lessons.models import Lesson, Product, ProductAccess, ProductLesson


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fileds = ('title', 'onwer')


class ProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccess
        fields = ('product', 'user')


class LessonSerializer(serializers.ModelSerializer):
    watched_time = serializers.SerializerMethodField()
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = (
            'title', 'video_link', 'duration', 'products', 'watched_time', 'is_viewed'
        )

        def get_watched_time(self, obj):
            start_time = 0
            end_time = obj.duration
            if start_time and end_time:
                watched_time = timedelta(end_time - start_time).total_seconds()
                return watched_time

        def get_is_viewed(self, obj):
            watched_percentage = (obj.watched_time / obj.duration) * 100
            return watched_percentage >= 80


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
