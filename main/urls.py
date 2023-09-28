from main.apps import MainConfig
from django.urls import path
from rest_framework.routers import DefaultRouter

from main.views import CoursesViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView

app_name = MainConfig.name
# роуетр для вьюсета ViewSet
router = DefaultRouter()
router.register(r'courses', CoursesViewSet, basename='courses')

# Паттерны для Generic уроков Lessons
urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/<int:pk>/detail/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),
] + router.urls
