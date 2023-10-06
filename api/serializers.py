from django.db.models import Q, Sum
from rest_framework import serializers

from lessons.models import Lesson, LessonView, Product, User


class ProductSerializer(serializers.ModelSerializer):
    viewed_lessons = serializers.SerializerMethodField()
    view_time = serializers.SerializerMethodField()
    students = serializers.SerializerMethodField()
    product_efficiency = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fileds = (
            'title', 'lessons_views', 'view_time', 'students',
            'product_efficiency'
        )

    def get_viewed_lessons(self, obj):
        user = self.context['request'].user
        return Lesson.objects.filter(
            Q(lesson_products__product=obj)
            & Q(lesson_products__product__user=user)
            & Q(lesson_products__is_viewed=True)
        ).count()

    def get_view_time(self, obj):
        user = self.context['request'].user
        total_view_time = Lesson.objects.filter(
            Q(lesson_products__product=obj)
            & Q(lesson_products__product__user=user)
            & Q(lesson_products__is_viewed=True)
        ).aggregate(total_view_time=Sum('duration'))['total_view_time']

        return total_view_time if total_view_time else 0

    def get_students(self, obj):
        return obj.product_accessed.all().count()

    def get_product_efficiency(self):
        return self.get_students() / User.objects.all().count()


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
