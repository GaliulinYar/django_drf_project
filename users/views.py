from rest_framework import permissions, viewsets
from users.permissions import IsOwnerOrReadOnly

from users.models import User
from users.serializers import UserSerializer, PublicUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet для пользователя"""

    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_serializer_class(self):
        """
        Определяем выбор сериалайзера для показа нужных полей в зависимости
        от того, является ли позьзователь собственником профиля
        """

        if self.request.user.pk == self.get_object().pk:
            return UserSerializer
        return PublicUserSerializer

    def perform_create(self, serializer):
        """ Позволяем создавать и редактировать только свой профиль """

        serializer.save(owner=self.request.user)
