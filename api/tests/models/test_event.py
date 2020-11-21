from django.test import TestCase
from ..factories import EventFactory
from api.models import Event


class EventModelTest(TestCase):
  def setUp(self):
    self.event1 = EventFactory(sport='Cycling')
    self.event2 = EventFactory(sport='Archery')
    self.event3 = EventFactory(sport='Archery')

  def test_string_representation(self):
    self.assertEqual(str(self.event1), self.event1.name)

  def test_all_sorted_by_sport(self):
    expected = [
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

    self.assertEqual(Event.all_sorted_by_sport(), expected)


