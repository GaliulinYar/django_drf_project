from rest_framework import serializers

from main.models import Courses, Lesson


class CoursesSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов"""
    class Meta:
        model = Courses
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для уроков"""
    class Meta:
        model = Lesson
        fields = '__all__'
