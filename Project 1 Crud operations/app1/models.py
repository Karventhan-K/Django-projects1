from django.db import models

# Create your models here.

class Account(models.Model):
    account_number = models.IntegerField(blank=True)
    account_name = models.CharField(max_length=30, default='')
    description  = models.CharField(max_length=100, default='')
    account_type = models.CharField(max_length=30, default='')
    opening_balance = models.CharField(max_length=30, default='')
    current_balance = models.CharField(max_length=30, default='')

