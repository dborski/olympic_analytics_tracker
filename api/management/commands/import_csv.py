from django.core.management.base import BaseCommand, CommandError
from api.models import Olympian, Event, EventOlympian
import csv
import time


class Command(BaseCommand):
  def __init__(self):
    self.file_location = './api/fixtures/olympic_data_2016.csv'

  def handle(self, *args, **options):
    print('Now starting import_csv script....')

    with open(self.file_location, 'r') as csvfile:
      reader = csv.DictReader(csvfile)
      total_time = 0.
      dot_string = ''

      for i, row in enumerate(reader):
        start = time.time()
        height = None if row['Height'] == 'NA' else int(row['Height'])
        weight = None if row['Weight'] == 'NA' else int(row['Weight'])

        olympian, oly_created = Olympian.objects.get_or_create(
          name=row['Name'],
          sex=row['Sex'],
          age=int(row['Age']),
          height=height,
          weight=weight,
          team=row['Team'],
          sport=row['Sport']
        )

        event, ev_created = Event.objects.get_or_create(
          name=row['Event'],
          games=row['Games'],
          sport=row['Sport']
        )

        EventOlympian.objects.get_or_create(
          event_id=event.id,
          olympian_id=olympian.id,
          medal=row['Medal']
        )

        if i % 700 == 0 and i != 0:
          dot_string = dot_string + '.'
          print(dot_string)
          
        stop = time.time()
        total_time += (stop - start)

    print(f'import_csv script has completed in {round(total_time, 2)} seconds')




      
