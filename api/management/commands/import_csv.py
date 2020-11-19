from django.core.management.base import BaseCommand, CommandError
from api.models import Olympian, Event, EventOlympian
import csv
import time


file_location = './api/fixtures/olympic_data_2016.csv'

class Command(BaseCommand):

  def handle(self, *args, **options):
    print('Now starting import_csv script....')

    with open(file_location, 'r') as csvfile:
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

        olympian.eventolympian_set.create(
          event_id=event.id, 
          medal=row['Medal']
        )

        stop = time.time()
        total_time += (stop - start)
        if i % 700 == 0 and i != 0:
          dot_string = dot_string + '.'
          print(dot_string)

    print(f'import_csv script has completed in {round(total_time, 2)} seconds')




      
