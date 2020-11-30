from django.core.management.base import BaseCommand, CommandError
from api.models import Olympian
import csv
from datetime import date
import time


class Command(BaseCommand):
  def __init__(self):
    self.file_location = f"./api/fixtures/olympians-{date.today().strftime('%Y-%m-%d')}.csv"

  def handle(self, *args, **options):
    print('Running export_csv script....')

    olympians = Olympian.all_olympians()[1]

    with open(self.file_location, 'w', newline='') as csvfile:
      field_names = ['Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'Sport', 'Medals Won']
      writer = csv.DictWriter(csvfile, fieldnames=field_names, dialect='excel')
      total_time = 0.

      writer.writeheader()
      for olympian in olympians:
        start = time.time()

        writer.writerow(
          {
            'Name': olympian.name,
            'Sex': olympian.sex,
            'Age': olympian.age,
            'Height': olympian.height,
            'Weight': olympian.weight,
            'Team': olympian.team,
            'Sport': olympian.sport,
            'Medals Won': olympian.medal_count
          }
        )

        stop = time.time()
        total_time += (stop - start)
      
      print(f'export_csv script completed in {round(total_time, 3)} seconds')



    
