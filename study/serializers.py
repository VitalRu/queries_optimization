from rest_framework import serializers

from .models import Lesson


class MyLessonsSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    view_time = serializers.IntegerField()

    class Meta:
        model = Lesson
        fields = ('title', 'status', 'view_time')


class MyLessonByProductSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    view_time = serializers.IntegerField()
    last_view_datetime = serializers.DateTimeField()

    class Meta:
        model = Lesson
        fields = ('title', 'status', 'view_time', 'last_view_datetime')
