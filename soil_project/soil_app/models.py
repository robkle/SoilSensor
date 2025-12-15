from django.db import models
from timescale.db.models.fields import TimescaleDateTimeField
from timescale.db.models.managers import TimescaleManager
from timescale.db.models.models import TimescaleModel
# Create your models here.

class TimescaleModel(models.Model):
    timestamp = TimescaleDateTimeField(interval="1 hour")
    objects = TimescaleManager()

    class Meta:
        abstract = True

class SensorData(TimescaleModel):
    sensor_id = models.IntegerField(primary_key=True)
    soil_moisture = models.FloatField()
    temperature = models.FloatField()