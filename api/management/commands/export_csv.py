from django.core.management.base import BaseCommand, CommandError
from api.models import Olympian
import csv
from datetime import date


class Command(BaseCommand):
  def __init__(self):
    self.file_location = f"./api/fixtures/olympians-{date.today().strftime('%Y-%m-%d')}.csv"

  def handle(self, *args, **options):
    print('Now starting export_csv script....')

    olympians = Olympian.all_olympians()[1]

    with open(self.file_location, 'w', newline='') as csvfile:
      field_names = ['Name', 'Sex', 'Age', 'Height', 'Weight', 'Team', 'Sport', 'Medals Won']
      writer = csv.DictWriter(csvfile, fieldnames=field_names, dialect='excel')

      writer.writeheader()
      for olympian in olympians:
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



    
