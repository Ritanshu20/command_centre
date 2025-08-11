from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import VideoAlert, SensorAlert
from .serializers import VideoAlertSerializer, SensorAlertSerializer
from django.utils.dateparse import parse_datetime
from datetime import timedelta

@api_view(['POST'])
def video_alert(request):
    serializer = VideoAlertSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def sensor_alert(request):
    serializer = SensorAlertSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def correlated_alerts(request):
    correlated = []
    for video in VideoAlert.objects.all():
        time_window_start = video.timestamp - timedelta(seconds=5)
        time_window_end = video.timestamp + timedelta(seconds=5)
        matching_sensors = SensorAlert.objects.filter(timestamp__range=(time_window_start, time_window_end))
        for sensor in matching_sensors:
            correlated.append({
                "video": VideoAlertSerializer(video).data,
                "sensor": SensorAlertSerializer(sensor).data
            })
    return Response(correlated)
