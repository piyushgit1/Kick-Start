from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.db import models

# Create your models here.

class UserProfile(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length= 50, unique= True)
    email = models.EmailField(max_length= 30)
    is_superuser = models.BooleanField(default= True)
    is_staff = models.BooleanField(default= True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username




