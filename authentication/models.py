from django.db import models

# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField


from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager



class CustomUserManager(BaseUserManager):


    def create_user(self, email, password, **extra_fields):
        
        

        if not email:
            raise("Email shoul be provide")
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
        
        
    
    
    
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff" , True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

   
        


        if extra_fields.get('is_staff') is not True:
            raise('Super User shoul have is_staff as True')
        
        if extra_fields.get('is_superuser') is not True:
            raise('Super User shoul have is_superuser as True')
        

        if extra_fields.get('is_staff') is not True:
            raise('Super User shoul have is_staff as True')
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=30, unique=True)
    phone_number = PhoneNumberField(null=False, unique=True)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS =['username', 'phone_number']

    objects = CustomUserManager()

    def __str__(self):
        return f'<User :{self.email}'
    