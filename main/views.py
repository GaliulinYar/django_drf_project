from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, generics

from main.models import Courses, Lesson
from main.serializers import CoursesSerializer, LessonSerializer


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