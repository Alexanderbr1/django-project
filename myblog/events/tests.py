from django.test import TestCase, Client
from .models import Event, EventLikes, Sport

class EventTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.sport = Sport.objects.create(name='Test Sport')
        self.event = Event.objects.create(
            title='Test Event',
            description='This is a test event',
            location='Test Location',
            date='2023-06-28',
            img='image/2023/test_image.jpg'
        )
        self.event.sports.add(self.sport)

    def test_event_view(self):
        response = self.client.get('/events/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/events.html')

    def test_event_detail_view(self):
        response = self.client.get(f'/events/{self.event.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/event_detail.html')
        self.assertEqual(response.context['event'], self.event)
        self.assertIn(self.sport, response.context['sports'])

