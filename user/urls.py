from django.urls import path

from .views import UserRegistrationAPIView, LoginAPIView

app_name = 'user'

urlpatterns = [
    path('users/', UserRegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]