import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, QueryDict
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

class OlympianList(APIView):
  def get(self, request):
    params = request.GET

    if params.__contains__('age'):
      olympians = Olympian.youngest_oldest_olympian(params['age'])
    else:
      olympians = Olympian.all_olympians()
    
    return JsonResponse(_olympians_payload(olympians), status=200)




