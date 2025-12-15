from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorDataViewSetPost, SensorDataViewSetGet

router = DefaultRouter()
router.register(r'data', SensorDataViewSetPost)
router.register(r'data/sensor', SensorDataViewSetGet)

urlpatterns = [
    path('', include(router.urls)),
]