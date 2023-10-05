from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserViewSet
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# Добавили связи с Юзером
app_name = UsersConfig.name

# роутер viewset user
router = DefaultRouter()
router.register(r'', UserViewSet, basename='users')

urlpatterns = [
    # паттерны для авторизации
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
