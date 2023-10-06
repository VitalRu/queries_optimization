from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from lessons.models import LessonView, Product, ProductAccess, ProductLesson


class ProductSerializer(serializers.ModelSerializer):
    lessons_views = serializers.SerializerMethodField()
    view_time = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    product_efficiency = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fileds = (
            'title', 'lessons_views', 'view_time', 'students',
            'product_efficiency'
        )

    def get_lessons_views(self):
        pass

    def get_view_time(self):
        pass

    def get_students(self):
        pass

    def get_product_efficiency(self):
        pass


class ProductAccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductAccess
        fields = ('product', 'user')


class LessonSerializer(serializers.ModelSerializer):
    title = serializers.ReadOnlyField(source='view_lesson.title')
    video_link = serializers.ReadOnlyField(source='view_lesson.video_link')
    duration = serializers.ReadOnlyField(source='view_lesson.duration')
    watched_time = serializers.SerializerMethodField()
    is_viewed = serializers.SerializerMethodField()

    class Meta:
        model = LessonView
        fields = (
            'title', 'video_link', 'duration', 'watched_time', 'is_viewed'
        )

        def get_watched_time(self, obj):
            return obj.view_duration

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
