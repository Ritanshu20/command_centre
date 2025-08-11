from rest_framework import serializers
from .models import VideoAlert, SensorAlert

class VideoAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoAlert
        fields = '__all__'

class SensorAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorAlert
        fields = '__all__'
