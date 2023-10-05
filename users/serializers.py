from rest_framework import serializers

from main.models import Payments
from main.serializers import PaymentsForOwnerSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для юзера"""

    # Вложенный сериализатор платежей
    payments = serializers.SerializerMethodField()

    class Meta:
        # показываем все поля
        model = User
        fields = '__all__'

    # Поля платежей по фильтру, только одного пользавателя
    def get_payments(self, owner):
        # Не показываем историю платежей, если пользователь не владелец
        if self.context['request'].user != owner:
            return None
        return PaymentsForOwnerSerializer(Payments.objects.filter(owner=owner), many=True).data


class PublicUserSerializer(serializers.ModelSerializer):
    """ Сериализатор для публичной информации о пользователе """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'role']
