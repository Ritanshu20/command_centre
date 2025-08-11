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

🔧 Setup Instructions

1 Clone the repository
```bash
git clone https://github.com/your-username/command-centre-backend.git
cd command-centre-backend





