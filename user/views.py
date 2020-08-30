from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .renderers import UserJSONRenderer
from rest_framework.authtoken.models import Token

from .serializers import (UserRegistrationSerializer,
						  LoginSerializer,
						  )
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.generics import CreateAPIView, ListAPIView


class UserRegistrationAPIView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = UserRegistrationSerializer

    def post(self, request):
        user = request.data.get('user', {})
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
 


#class LoginAPIView(APIView):
#    permission_classes = (AllowAny,)
#    renderer_classes = (UserJSONRenderer,)
#    serializer_class = LoginSerializer
#
#    def post(self, request):
#        user = request.data.get('user', {})
#        #user = authenticate(username=email, password=password)
#        token, created = Token.objects.get_or_create(user=user)
#        serializer = self.serializer_class(data=user)
#        serializer.is_valid(raise_exception=True)
#
#        return Response(serializer.data, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))

def login(request):

    email = request.data.get("email")
    password = request.data.get("password")
    print(email, password)

    if email is None or password is None:
        return Response({'error': 'Убедитесь в правильности вводимых данных'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=email, password=password)
    if not user:
        return Response({'error': 'Убедитесь в правильности вводимых данных'},
                        status=HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)