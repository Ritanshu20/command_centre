from django.db import models

class VideoAlert(models.Model):
    camera_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    event_type = models.CharField(max_length=100)
    confidence = models.FloatField()

    def __str__(self):
        return f"{self.event_type} - {self.camera_id}"


class SensorAlert(models.Model):
    sensor_id = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    reading = models.FloatField()
    unit = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.sensor_id} - {self.reading}{self.unit}"
