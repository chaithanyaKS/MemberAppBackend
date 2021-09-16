# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    GENDER = (
        ("male", "Male"),
        ("female", "Female"),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255, blank=True)
    date_of_birth = models.DateField(blank=True)
    gender = models.CharField(max_length=10, choices=GENDER, blank=True)
    address_1 = models.TextField(blank=True)
    address_2 = models.TextField(blank=True)
    phone_address = models.CharField(max_length=10, blank=True)
