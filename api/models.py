from django.db import models
from django.db.models import Count, Avg, Q, F
import api.payloads as pl


class Olympian(models.Model):
  GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
  ]
  name = models.CharField(max_length=100)
  sex = models.CharField(max_length=1, choices=GENDER)
  age = models.IntegerField(blank=True, null=True)
  height = models.IntegerField(blank=True, null=True)
  weight = models.IntegerField(blank=True, null=True)
  team = models.CharField(max_length=100)
  sport = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
  @classmethod
  def all_olympians(cls):

    olympians = Olympian.objects.annotate(
        medal_count=Count('eventolympian__medal', filter=Q(eventolympian__medal__in=EventOlympian.medal_choices()))
    ).order_by('name')

    return [pl.olympian_payload(olympian) for olympian in olympians]

  @classmethod
  def youngest_oldest_olympian(cls, age):
    order = 'age' if age == 'youngest' else '-age'

    olympians = Olympian.objects.annotate(
        medal_count=Count('eventolympian__medal', filter=Q(eventolympian__medal__in=EventOlympian.medal_choices()))
    ).order_by(order)[:1]

    return [pl.olympian_payload(olympian) for olympian in olympians]

  @classmethod
  def olympian_stats(cls):
    return Olympian.objects.aggregate(
        total_olympians=Count('id'),
        avg_age=Avg('age'),
        male_avg=Avg('weight', filter=Q(sex='M')),
        female_avg=Avg('weight', filter=Q(sex='F'))
    )
  
  @classmethod
  def medalists_by_event(cls, event_id):
    olympians = Olympian.objects.filter(
        eventolympian__event_id=event_id
    ).annotate(
        medal=F('eventolympian__medal')
    ).filter(
      Q(medal__in=EventOlympian.medal_choices())
    ).order_by('name')

    return [pl.event_medalists_payload(olympian) for olympian in olympians]


class Event(models.Model):
  name = models.CharField(max_length=100)
  games = models.CharField(max_length=100)
  sport = models.CharField(max_length=100)
  olympians = models.ManyToManyField(
      Olympian,
      through='EventOlympian',
      through_fields=('event', 'olympian')
  )
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
  
  @classmethod
  def all_sorted_by_sport(cls):
    sports = Event.objects.values_list('sport', flat=True)
    unique_sports = sorted(list(set(sports)))
    sorted_events = []

    for sport in unique_sports:
      events = Event.objects.filter(sport=sport)
      sorted_events.append(pl.event_sports_payload(sport, events))

    return sorted_events


class EventOlympian(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  olympian = models.ForeignKey(Olympian, on_delete=models.CASCADE)
  medal = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  @classmethod
  def medal_choices(cls):
    return [
      'Gold',
      'Silver',
      'Bronze'
    ]


