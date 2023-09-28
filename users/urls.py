from django.urls import path

from users.apps import UsersConfig
from users.views import UserUpdateAPIView, UserListAPIView

# Добавили связи с Юзером
app_name = UsersConfig.name

urlpatterns = [
    # паттерн для обновления юзера
    path('user/update/<int:pk>', UserUpdateAPIView.as_view(), name='user_update'),
    # паттерн для просмотра
    path('user/', UserListAPIView.as_view(), name='user_list'),
]
