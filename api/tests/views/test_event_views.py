from django.test import TestCase
from ..factories import EventFactory, OlympianFactory, EventOlympianFactory


class EventViewSet(TestCase):
  def setUp(self):
    self.olympian1 = OlympianFactory(name='Allie')
    self.olympian2 = OlympianFactory(name='Holly')
    self.olympian3 = OlympianFactory(name='Jim')
    self.olympian4 = OlympianFactory(name='Sal')
    self.olympian5 = OlympianFactory(name='Kate')

    self.event1 = EventFactory(sport='Cycling')
    self.event2 = EventFactory(sport='Archery')
    self.event3 = EventFactory(sport='Archery')

    self.event_olympian1 = EventOlympianFactory(event=self.event1, olympian=self.olympian1, medal='NA')
    self.event_olympian2 = EventOlympianFactory(event=self.event1, olympian=self.olympian2, medal='Bronze')
    self.event_olympian3 = EventOlympianFactory(event=self.event1, olympian=self.olympian3, medal='Gold')
    self.event_olympian4 = EventOlympianFactory(event=self.event1, olympian=self.olympian4, medal='Silver')

    self.event_olympian5 = EventOlympianFactory(event=self.event2, olympian=self.olympian5, medal='Silver')

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

  def test_happy_path_get_medalists_by_event(self):
    response = self.client.get(f'/api/v1/events/{self.event1.id}/medalists')

    json_response = response.json()

    expected = {
        'event': self.event1.name,
        'medalists': [
            {
                'name': self.olympian2.name,
                'team': self.olympian2.team,
                'age': self.olympian2.age,
                'medal': 'Bronze'
            },
            {
                'name': self.olympian3.name,
                'team': self.olympian3.team,
                'age': self.olympian3.age,
                'medal': 'Gold'
            },
            {
                'name': self.olympian4.name,
                'team': self.olympian4.team,
                'age': self.olympian4.age,
                'medal': 'Silver'
            }
        ]
    }

    self.assertEqual(json_response, expected)
