from django.db import models
from django.contrib.auth.models import AbstractUser
from ads.models import Ad


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.email


class Visitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user.is_staff = False
    ads_watched = models.ManyToManyField(Ad)

    def __str__(self):
        return self.user.email


class Advertiser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    user.is_staff = True
    ads_created = models.ForeignKey(Ad, on_delete=models.DO_NOTHING, default=None)

    def __str__(self):
        return self.user.email
