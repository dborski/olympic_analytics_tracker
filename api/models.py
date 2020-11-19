from django.db import models


class Olympian(models.Model):
  GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other')
  ]
  name = models.CharField(max_length=100)
  sex = models.CharField(max_length=1, choices=GENDER)
  age = models.IntegerField()
  height = models.IntegerField()
  weight = models.IntegerField()
  team = models.CharField(max_length=100)
  sport = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name
    
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

