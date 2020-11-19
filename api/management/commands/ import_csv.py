from django.core.management.base import BaseCommand, CommandError
from api.models import Olympian, Event, EventOlympian


class Command(BaseCommand):
  ''
