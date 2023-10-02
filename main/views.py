from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter

from main.models import Courses, Lesson, Payments
from main.serializers import CoursesSerializer, LessonSerializer, PaymentsSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    """ViewSet для модели курса Courses"""
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()


class LessonCreateAPIView(generics.CreateAPIView):
    """Generic создания урока Lesson"""
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """Generic просмотра всех уроков Lesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Generic одного урокаLesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Generic для обновления урока Lesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Generic для удаления одного урока Lesson"""
    queryset = Lesson.objects.all()


# Вьюшки для платежей
class PaymentsListAPIView(generics.ListAPIView):
    """ Generic-класс для вывода списка платежей """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    # Фильтр по полям
    filterset_fields = ('course_pay', 'lesson_pay', 'owner', 'method',)
    # Фильтр по датее
    ordering_fields = ('date_pay',)


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    """ Generic-класс для просмотра всех платежей одного юзера """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
