from rest_framework import permissions

from users.models import UserRoles


class IsModeratorOrReadOnly(permissions.BasePermission):
    """ Разрешение модераторам на просмотр"""

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == UserRoles.MODERATOR


class IsCourseOwner(permissions.BasePermission):
    """ Разрешение для владельцев только курсы """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsCourseOrLessonOwner(permissions.BasePermission):
    """ Разрешение для владельцев только курсы и уроки """

    def has_object_permission(self, request, view, obj):
        return obj.course.owner == request.user or obj.course.lesson_set.filter(owner=request.user).exists()


class IsPaymentOwner(permissions.BasePermission):
    """ Для владельцев платежа"""

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user
