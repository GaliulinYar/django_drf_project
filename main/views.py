from rest_framework.exceptions import PermissionDenied
from rest_framework.fields import SerializerMethodField
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated

from main.models import Courses, Lesson, Payments
from main.permissions import IsModeratorOrReadOnly, IsCourseOwner, IsPaymentOwner
from main.serializers import CourseSerializer, LessonSerializer, PaymentsSerializer
from users.models import UserRoles


class CoursesViewSet(viewsets.ModelViewSet):
    """Сериализатор для курсов"""
    lessons = CourseSerializer
    permission_classes = [IsAuthenticated, IsModeratorOrReadOnly | IsCourseOwner]

    class Meta:
        model = Courses
        fields = '__all__'

    def get_queryset(self):
        """ Делаем доступ к объектам только для владельцев(создателей) """

        if self.request.user.role == UserRoles.MODERATOR:
            return Courses.objects.all()
        else:
            return Courses.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        """ Запрещаем модераторам создавать курсы """

        if self.request.user.role == UserRoles.MODERATOR:
            raise PermissionDenied("Вам нельзя создавать курсы")
        else:
            new_payment = serializer.save()
            new_payment.owner = self.request.user
            new_payment.save()

    def perform_destroy(self, instance):
        """ Запрещаем модераторам удалять курсы """

        if self.request.user.role == UserRoles.MODERATOR:
            raise PermissionDenied("Вам нельзя удалять курсы!")
        instance.delete()


class LessonCreateAPIView(generics.CreateAPIView):
    """Generic создания урока Lesson"""
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsPaymentOwner]

    def perform_create(self, serializer):
        """ Запрещаем модераторам создавать уроки """
        if self.request.user.role == UserRoles.MODERATOR:
            raise PermissionDenied("Вы не можете создавать уроки")
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    """Generic просмотра всех уроков Lesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsPaymentOwner]

    def get_queryset(self):
        """ Открываем доступ только владельцам и модераторам """

        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """Generic одного урокаLesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()

    def get_queryset(self):
        """ Открываем доступ только владельцам и модераторам """

        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonUpdateAPIView(generics.UpdateAPIView):
    """Generic для обновления урока Lesson"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsPaymentOwner]

    def get_queryset(self):
        """ Открываем доступ только владельцам и модераторам """

        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonDestroyAPIView(generics.DestroyAPIView):
    """Generic для удаления одного урока Lesson"""
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsPaymentOwner]

    def get_queryset(self):
        """ Открываем доступ только владельцам и модераторам """

        if self.request.user.role == UserRoles.MODERATOR:
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)

    def perform_destroy(self, instance):
        """ Запрещаем модераторам удалять объект """

        if self.request.user.role == UserRoles.MODERATOR:
            raise PermissionDenied("Вам нельзя удалять уроки")
        instance.delete()


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
    permission_classes = [IsAuthenticated, IsModeratorOrReadOnly | IsPaymentOwner]

    def get_queryset(self):
        """ Посмотреть платежи могут только владельцы и модераторы """

        if self.request.user.role == UserRoles.MODERATOR:
            return Payments.objects.all()
        else:
            return Payments.objects.filter(owner=self.request.user)


class PaymentsRetrieveAPIView(generics.RetrieveAPIView):
    """ Generic-класс для просмотра всех платежей одного юзера """

    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()
    permission_classes = [IsAuthenticated, IsModeratorOrReadOnly | IsPaymentOwner]

    def get_queryset(self):
        """ Посмотреть платежи могут только владельцы и модераторы """

        if self.request.user.role == UserRoles.MODERATOR:
            return Payments.objects.all()
        else:
            return Payments.objects.filter(owner=self.request.user)
