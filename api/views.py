from django.http import JsonResponse
from rest_framework.views import APIView
from api.models import Olympian


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

    if params.__contains__('age'):
      olympians = Olympian.youngest_oldest_olympian(params['age'])
    else:
      olympians = Olympian.all_olympians()
    
    return JsonResponse(_olympians_payload(olympians), status=200)


class OlympianStats(APIView):
  def get(self, request):
    olympian_stats = Olympian.olympian_stats()
     
    return JsonResponse(_olympian_stats_payload(olympian_stats), status=200)
