from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from rest_framework.relations import SlugRelatedField

from main.models import Courses, Lesson, Payments
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для уроков"""
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    """Сериализатор для уроков которые будут показываться при выводе КУРСОВ"""
    class Meta:
        model = Lesson
        fields = ['lesson_name', 'lesson_description']


# Для сериализатора модели курса реализуйте поле вывода уроков.
class CoursesSerializer(serializers.ModelSerializer):
    """Сериализатор для курсов"""
    lessons = SerializerMethodField()

    class Meta:
        model = Courses
        fields = '__all__'

    # Получаем все поля для дополнительного поля уроков с фильтрацией по курсу
    def get_lessons(self, course_lesson):
        return LessonListSerializer(Lesson.objects.filter(course_lesson=course_lesson), many=True).data


# Сериалайзеры для платежей Payments
class PaymentsSerializer(serializers.ModelSerializer):
    """Класс-сериализотор для модели платежей Payments"""

    course_pay = SlugRelatedField(slug_field='name', queryset=Courses.objects.all())
    lesson_pay = SlugRelatedField(slug_field='name', queryset=Lesson.objects.all())
    owner = SlugRelatedField(slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Payments
        fields = '__all__'


class PaymentsForOwnerSerializer(serializers.ModelSerializer):
    """Класс-сериализотор платежей для вывода у одного пользователя"""

    class Meta:
        model = Payments
        fields = ['id', 'course_pay', 'lesson_pay', 'owner', 'date_pay', 'sum_pay', 'way_pay']
