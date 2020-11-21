import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, QueryDict
from rest_framework.views import APIView
from api.models import Olympian

from django.db.models import Avg, Count

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

def _olympian_stats_payload(count, m_weight, f_weight, age):
  return {
      'olympian_stats': {
        'total_competing_olympians': count,
        'average_weight': {
          'unit': 'kg',
          'male_olympians': m_weight,
          'female_olympians': f_weight
        },
        'average_age': age
      }
  }

class OlympianList(APIView):
  def get(self, request):
    params = request.GET

    if params.__contains__('age'):
      olympians = Olympian.youngest_oldest_olympian(params['age'])
    else:
      olympians = Olympian.all_olympians()
    
    return JsonResponse(_olympians_payload(olympians), status=200)


class OlympianStats(APIView):
  def get(self, request):

    #Need to calculate 4 things:
    # total count of all olympians
    count_avg = Olympian.objects.aggregate(Count('id'), Avg('age')) 
    # average weight of all male olympians
    male_weight = Olympian.objects.filter(sex='M').aggregate(Avg('weight'))
    # average weight of all female olympians
    female_weight = Olympian.objects.filter(sex='F').aggregate(Avg('weight'))

    # then return it in the pre_built payload
    import code; code.interact(local=dict(globals(), **locals()))
     
    return JsonResponse(_olympian_stats_payload(count_avg['id__count'], male_weight, female_weight, count_avg['id__count']), status=200)
