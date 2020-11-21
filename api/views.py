from django.http import JsonResponse
from rest_framework.views import APIView
from api.models import Olympian, Event
from django.core.exceptions import ObjectDoesNotExist


def _error_payload(error, code=400):
  return {
      'success': False,
      'error': code,
      'errors': error
  }

def _olympians_payload(olympians):
  return {
      'olympians': olympians
  }

def _events_payload(events):
  return {
      'events': events
  }

def _medalists_payload(event, medalists):
  return {
      'event': event,
      'medalists': medalists
  }

def _olympian_stats_payload(stats):
  return {
      'olympian_stats': {
        'total_competing_olympians': stats['total_olympians'],
        'average_weight': {
          'unit': 'kg',
          'male_olympians': round(stats['male_avg'], 1),
          'female_olympians': round(stats['female_avg'], 1)
        },
        'average_age': round(stats['avg_age'], 1)
      }
  }


class OlympianList(APIView):
  def get(self, request):
    params = request.GET
    age_params = ['youngest', 'oldest']

    if params.__contains__('age') and params['age'] in age_params:
      olympians = Olympian.youngest_oldest_olympian(params['age'])

    elif not params.__contains__('age'):
      olympians = Olympian.all_olympians()

    else:
      error = "The age query parameter must equal 'youngest' or 'oldest'"
      return JsonResponse(_error_payload(error), status=400)
    
    return JsonResponse(_olympians_payload(olympians), status=200)


class OlympianStats(APIView):
  def get(self, request):
    olympian_stats = Olympian.olympian_stats()
     
    return JsonResponse(_olympian_stats_payload(olympian_stats), status=200)


class EventList(APIView):
  def get(self, request):
    all_events = Event.all_sorted_by_sport()

    return JsonResponse(_events_payload(all_events), status=200)


class EventMedalists(APIView):
  def get(self, request, pk):
    try:
      event = Event.objects.get(id=pk)
    except ObjectDoesNotExist:
      return JsonResponse(_error_payload('No event found by that ID'), status=404)

    medalists = Olympian.medalists_by_event(pk)
    event_name = event.name

    return JsonResponse(_medalists_payload(event_name, medalists), status=200)
