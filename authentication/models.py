from django.db import models

# Create your models here.

import os
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("User Most Have An Email")
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Super User Must Have is_taff = True")
        

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Super User Must Have is_superuser = True")

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f'<User :{self.email}'
    