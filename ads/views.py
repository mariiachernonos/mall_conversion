from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, DestroyAPIView, UpdateAPIView
from . import models
from . import serializers


class AdListCreateAPIView(ListCreateAPIView):
    queryset = models.Ad.objects.all()
    serializer_class = serializers.AdSerializer

# class AdUpdateAPIView(UpdateAPIView):



