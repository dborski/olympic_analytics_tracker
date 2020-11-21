import json
from django.test import TestCase
from ..factories import OlympianFactory, EventFactory, EventOlympianFactory


class OlympianViewSet(TestCase):
  def setUp(self):
    self.olympian1 = OlympianFactory(name='Curtis', age=22, sex='M', weight=123)
    self.olympian2 = OlympianFactory(name='Albert', age=19, sex='F', weight=150)
    self.olympian3 = OlympianFactory(name='Billy', age=30, sex='M', weight=208)

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

    json_response = response.json()

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
    self.assertEqual(json_response, expected)

  def test_happy_path_get_youngest_olympian(self):
    response = self.client.get('/api/v1/olympians?age=youngest')

    json_response = response.json()

    expected = {
      'olympians': [
        {
          'name': self.olympian2.name,
          'team': self.olympian2.team,
          'age': self.olympian2.age,
          'sport': self.olympian2.sport,
          'total_medals_won': 2
        }
      ]
    }

    self.assertEqual(response.status_code, 200)
    self.assertEqual(json_response, expected)

  def test_happy_path_get_oldest_olympian(self):
    response = self.client.get('/api/v1/olympians?age=oldest')

    json_response = response.json()

    expected = {
      'olympians': [
        {
          'name': self.olympian3.name,
          'team': self.olympian3.team,
          'age': self.olympian3.age,
          'sport': self.olympian3.sport,
          'total_medals_won': 0
        }
      ]
    }

    self.assertEqual(response.status_code, 200)
    self.assertEqual(json_response, expected)

  def test_happy_path_get_olympian_stats(self):
    response = self.client.get('/api/v1/olympian_stats')

    json_response = response.json()

    expected = {
      'olympian_stats': {
        'total_competing_olympians': 3,
        'average_weight': {
          'unit': 'kg',
          'male_olympians': 165.5,
          'female_olympians': 150.0
        },
        'average_age': 23.7
      }
    }

    self.assertEqual(response.status_code, 200)
    self.assertEqual(json_response, expected)
