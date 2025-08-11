from django.urls import path
from . import views

urlpatterns = [
  path('video-alert/', views.video_alert),
  path('sensor-alert/', views.sensor_alert),
  path('correlated-alerts/', views.correlated_alerts),
]
