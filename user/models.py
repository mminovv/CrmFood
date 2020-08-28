from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

from django.db import models
from service.models import Roles 

import jwt


class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username')

        if email is None:
            raise TypeError('Users must have an email')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password, **kwargs):
        if password is None:
            raise ValueError('Users must have password')

        user = self.create_user(username=username,password=password,email=self.normalize_email(email))
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=120, unique=True, default='Aziz')
    surname = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, unique=True)
    password = models.CharField(max_length=120, blank=False)
    #role = models.ForeignKey(Roles, on_delete=models.CASCADE, default='Admin')
    phone = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True, null=True)

    username = models.CharField(max_length=120, blank=False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'surname', 'email', 'password', 'phone']

    objects = UserManager()

    def __str__(self):
        return self.name    
        

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        day = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(day.strftime('%S'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')