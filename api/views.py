from django.http import JsonResponse
from rest_framework.views import APIView
from api.models import Olympian, Event
from django.core.exceptions import ObjectDoesNotExist
import api.payloads as pl


class OlympianList(APIView):
  def get(self, request):
    params = request.GET
    age_params = ['youngest', 'oldest']

    if params.__contains__('age') and params['age'] in age_params:
      try:
        olympians = Olympian.youngest_oldest_olympian(params['age'])
      except:
        return JsonResponse(pl.error_payload('There was an error in the request', 404), status=404)

    elif not params.__contains__('age'):
      try:
        olympians = Olympian.all_olympians()[0]
      except:
        return JsonResponse(pl.error_payload('There was an error in the request', 404), status=404)

    else:
      error = "The age query parameter must equal 'youngest' or 'oldest'"
      return JsonResponse(pl.error_payload(error), status=400)
    
    return JsonResponse(pl.olympians_payload(olympians), status=200)


class OlympianStats(APIView):
  def get(self, request):
    try:
      olympian_stats = Olympian.olympian_stats()
    except:
      return JsonResponse(pl.error_payload('There was an error in the request', 404), status=404)
     
    return JsonResponse(pl.olympian_stats_payload(olympian_stats), status=200)


class EventList(APIView):
  def get(self, request):
    try:
      all_events = Event.all_sorted_by_sport()
    except:
      return JsonResponse(pl.error_payload('There was an error in the request', 404), status=404)

    return JsonResponse(pl.events_payload(all_events), status=200)


class EventMedalists(APIView):
  def get(self, request, pk):
    try:
      event = Event.objects.get(pk=pk)
    except ObjectDoesNotExist:
      return JsonResponse(pl.error_payload('No event found by that ID', 404), status=404)

    event_name = event.name
    medalists = Olympian.medalists_by_event(pk)

    return JsonResponse(pl.medalists_payload(event_name, medalists), status=200)
