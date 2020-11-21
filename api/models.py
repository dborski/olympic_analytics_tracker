from django.db import models
from django.db.models import Count, Avg, Q

def _olympian_payload(olympian):
  return {
      'name': olympian.name,
      'team': olympian.team,
      'age': olympian.age,
      'sport': olympian.sport,
      'total_medals_won': olympian.medal_count
  }

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
    medals = ['Gold', 'Silver', 'Bronze']

    olympians = Olympian.objects.annotate(
        medal_count=Count('eventolympian__medal', filter=Q(eventolympian__medal__in=medals))
    ).order_by('name')

    return [_olympian_payload(olympian) for olympian in olympians]

  @classmethod
  def youngest_oldest_olympian(cls, age):
    order = 'age' if age == 'youngest' else '-age'
    medals = ['Gold', 'Silver', 'Bronze']

    olympians = Olympian.objects.annotate(
        medal_count=Count('eventolympian__medal', filter=Q(eventolympian__medal__in=medals))
    ).order_by(order)[:1]

    return [_olympian_payload(olympian) for olympian in olympians]

  @classmethod
  def olympian_stats(cls):
    return Olympian.objects.aggregate(
        total_olympians=Count('id'),
        avg_age=Avg('age'),
        male_avg=Avg('weight', filter=Q(sex='M')),
        female_avg=Avg('weight', filter=Q(sex='F'))
    )


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


class EventOlympian(models.Model):
  event = models.ForeignKey(Event, on_delete=models.CASCADE)
  olympian = models.ForeignKey(Olympian, on_delete=models.CASCADE)
  medal = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

