from django.test import TestCase
from api.models import Event, Olympian, EventOlympian


class EventOlympianTest(TestCase):
  def setUp(self):
    self.event1 = Event.objects.create(name='event1', games='2016 Summer', sport='Badminton')
    self.olympian1 = Olympian.objects.create(name='olympian1', sex='M', age=30, height=160, weight=55, team='Spain', sport='Gymnastics')
    self.eventolympian1 = self.olympian1.eventolympian_set.create(event_id=self.event1.id, medal='Silver')

  def test_instance_of_eventolympian(self):
    self.assertEqual(self.eventolympian1.medal, 'Silver')

  def test_model_choices(self):
    expected = ['Gold', 'Silver', 'Bronze']

    self.assertEqual(EventOlympian.medal_choices(), expected)