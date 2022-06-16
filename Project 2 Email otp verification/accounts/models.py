
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


# This table is used for signup, login, and authentication process.
class User(AbstractUser):
    email = models.EmailField(unique=False)
    username = models.CharField(max_length=30, unique=False)
    phonenumber  = models.CharField(max_length=20, unique=True,default="")
    # country_code = models.CharField(max_length=20, unique=True,default="")
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.DateTimeField(default=timezone.now)
    modified_by = models.DateTimeField(default=timezone.now)
    otp = models.CharField(max_length=100, default="")
    is_verified = models.BooleanField(default=False)

    USERNAME_FIELD = 'phonenumber'