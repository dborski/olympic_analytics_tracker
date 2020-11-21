from django.test import TestCase
from ..factories import EventFactory


class EventViewSet(TestCase):
  def setUp(self):
    self.event1 = EventFactory(sport='Cycling')
    self.event2 = EventFactory(sport='Archery')
    self.event3 = EventFactory(sport='Archery')

  def test_happy_path_get_events_by_sport(self):
    response = self.client.get('/api/v1/events')

    json_response = response.json()

    expected = {
      'events':
        [
          {
            'sport': 'Archery',
            'events': [
              self.event2.name,
              self.event3.name,
            ]
          },
          {
            'sport': 'Cycling',
            'events': [
              self.event1.name,
            ]
          }
        ]
    }

    self.assertEqual(json_response, expected)
