from ads.serializers import AdSerializer
from users.models import User, Visitor, Advertiser
from django.db.models import Model
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'username', 'is_staff']


class VisitorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    ads_watched = AdSerializer(read_only=True, many=True)

    class Meta:
        model = Visitor
        fields = ['user', 'ads_watched']


class AdvertiserSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Advertiser
        fields = ['user', 'ads_created']
