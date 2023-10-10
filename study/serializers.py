from rest_framework import serializers

from study.models import Lesson, LessonViesInfo


class MyLessonsViewInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LessonViesInfo
        fields = ('status', 'view_time')


class MyLessonsSerializer(serializers.ModelSerializer):
    view_info = serializers.SerializerMethodField()

    def get_view_info(self, obj):
        view_info = LessonViesInfo.objects.get

    class Meta:
        models = Lesson
        fields = ('title',) 
