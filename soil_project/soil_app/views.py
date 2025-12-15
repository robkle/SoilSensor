from django.shortcuts import render
from rest_framework import viewsets
from .models import SensorData
from .serializers import SensorDataSerializer

# Create your views here.

class SensorDataViewSet(viewsets.ModelViewSet):
    queryset = SensorData
    serializer_class = SensorDataSerializer

class SensorDataViewSetPost(SensorDataViewSet):
    http_method_names = ['post']

class SensorDataViewSetGet(SensorDataViewSet):
    http_method_names = ['get', 'head']