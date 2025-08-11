from django.test import TestCase, Client
import json

class AlertsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_correlation(self):
        v = {...}  # same payload
        s = {...}
        self.client.post('/video-alert/', data=json.dumps(v), content_type='application/json')
        self.client.post('/sensor-alert/', data=json.dumps(s), content_type='application/json')
        r = self.client.get('/correlated-alerts/?seconds=5')
        self.assertEqual(r.status_code,200)
        self.assertTrue(len(r.json())>=1)
