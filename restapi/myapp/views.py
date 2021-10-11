from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

from myapp.models import Senator

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_senator(request, senator_name):
    if request.method == 'GET':
        try:
            Senator = Senator.objects.get(name=Senator_name)
            response = json.dumps([{ 'Senator': Senator.Senatorname, 'Tickername': Senator.Tickername, 'number_of_stocks': Senator.number_of_stocks, 'date': Senator.date}])
        except:
            response = json.dumps([{ 'Error': 'No Senator with that name'}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def add_senator(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        Senatorname = payload['Senatorname']
        Tickername = payload['Tickername']
        number_of_stocks = payload['number_of_stocks']
        date = payload['date']
        Senator = Senator(name=Senatorname, Tickername=Tickername, number_of_stocks = number_of_stocks, date = date)
        try:
            Senator.save()
            response = json.dumps([{ 'Success': 'Senator added successfully!'}])
        except:
            response = json.dumps([{ 'Error': 'Senator could not be added!'}])
    return HttpResponse(response, content_type='text/json')