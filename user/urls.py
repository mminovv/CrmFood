from django.urls import path
from .views import UserRegistrationAPIView, login #LoginAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'user'

urlpatterns = [
    path('users/', UserRegistrationAPIView.as_view()),
    #path('users/login/', LoginAPIView.as_view()),
    path('users/login/', login),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
