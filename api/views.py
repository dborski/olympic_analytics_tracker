import json
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.views import APIView
from api.models import Olympian
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist


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
    # Build a custom Olympian class function that
    # Pulls out all olympians from the db, including their total
    # medal count
    # This method must turn an array of hashes

    # Total medal count will have to be caluclated with join
    # to event_olympian table and counting medals
    
    # if request.GET['age']:
    #   ''
    # else:
    olympians = Olympian.all_olympians()
    return JsonResponse(_olympians_payload(olympians), status=200)


    # return JsonResponse(_error_payload(error), status=400)

