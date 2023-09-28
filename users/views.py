from rest_framework import generics

from users.models import User
from users.serializers import UserSerializer


class UserUpdateAPIView(generics.UpdateAPIView):
    """Класс Generic для обновления пользователя"""
    # Наборы атрибутов для класса
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    """Класс Generic для просмотра пользователей"""
    # Наборы атрибутов для класса
    serializer_class = UserSerializer
    queryset = User.objects.all()
