from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from mall_conversion.ads.models import Ad


class Visitor(AbstractUser):
    id = models.AutoField()
    username = models.CharField(max_length=30, unique=True)
    is_staff = False

    def __str__(self):
        return self.email


class Advertiser(AbstractUser):
    id = models.AutoField()
    username = models.CharField(max_length=30, unique=True)
    is_staff = True

    def __str__(self):
        return self.email
