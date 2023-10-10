from rest_framework import serializers

from study.models import Lesson, LessonViewInfo


class MyLessonsViewInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonViewInfo
        fields = ('status', 'view_time')


class MyLessonsSerializer(serializers.ModelSerializer):
    status = serializers.CharField()
    view_time = serializers.IntegerField()

    class Meta:
        models = Lesson
        fields = ('title', 'view_info')
