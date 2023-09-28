from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для юзера"""
    class Meta:
        # мета класс для перехвата всех полей юзера
        model = User
        fields = '__all__'
        