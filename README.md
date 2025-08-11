# Command Centre Backend (Django)
Description
This is a **Django REST API** backend for a Command Centre application.  
It processes alerts from:
- Video Monitoring – camera alerts, e.g., Intrusion Detection.
- Sensor Platform – temperature or other readings.

Your project will have a service that will allow you to **correlate** video and sensor alerts within **5 seconds** of each other.  
It will also apply **severity levels** for alerting, depending on the type of event and the sensor readings.

---

 Capabilities
1. POST `/video-alert` → Store video alerts from cameras.
2. POST `/sensor-alert` → Store sensor readings.
3. GET `/correlated-alerts` → Get video + sensor alerts within 5 seconds of each other.
4. Optional Severity:
   - Intrusion + higher temperature = Critical level.
   - Suspicious Movement = Medium level.
   - Normal reading(s) = Low level.

---

---

Logic & Approach
Models


VideoAlert: will store camera alerts.


SensorAlert: will store sensor readings.


Serializers


Validate incoming JSON and convert it into model instances.


Views


On making POST requests will store alerts.


Compare timestamps to check correlation.


Severity levels (optional)


If event_type == Intrusion and reading > 50°C → Critical.


If event_type == Suspicious Movement → Medium.


Otherwise → Low.
