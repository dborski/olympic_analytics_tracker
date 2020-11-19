import json
from django.test import TestCase
from ..factories import OlympianFactory, EventFactory, EventOlympianFactory


class OlympianViewSet(TestCase):
  def setUp(self):
    self.olympian1 = OlympianFactory(name='Curtis')
    self.olympian2 = OlympianFactory(name='Albert')
    self.olympian3 = OlympianFactory(name='Billy')

    self.event1 = EventFactory()
    self.event2 = EventFactory()

    self.event_olympian1 = EventOlympianFactory(event=self.event1, olympian=self.olympian1, medal='NA')
    self.event_olympian2 = EventOlympianFactory(event=self.event2, olympian=self.olympian1, medal='Bronze')

    self.event_olympian3 = EventOlympianFactory(event=self.event1, olympian=self.olympian2, medal='Silver')
    self.event_olympian4 = EventOlympianFactory(event=self.event2, olympian=self.olympian2, medal='Silver')

    self.event_olympian5 = EventOlympianFactory(event=self.event1, olympian=self.olympian3, medal='NA')
    self.event_olympian6 = EventOlympianFactory(event=self.event2, olympian=self.olympian3, medal='NA')


  def test_happy_path_get_all_olympians(self):
    response = self.client.get('/api/v1/olympians')

    expected = {
      'olympians': [
        {
          'name': self.olympian2.name,
          'team': self.olympian2.team,
          'age': self.olympian2.age,
          'sport': self.olympian2.sport,
          'total_medals_won': 2
        },
        {
          'name': self.olympian3.name,
          'team': self.olympian3.team,
          'age': self.olympian3.age,
          'sport': self.olympian3.sport,
          'total_medals_won': 0
        },
        {
          'name': self.olympian1.name,
          'team': self.olympian1.team,
          'age': self.olympian1.age,
          'sport': self.olympian1.sport,
          'total_medals_won': 1
        }
      ]
    }

    self.assertEqual(response.status_code, 200)
    self.assertEqual(response.data, expected)
