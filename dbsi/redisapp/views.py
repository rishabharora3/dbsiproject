from django.shortcuts import render
from django.core.cache import cache

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from .config import Config
from django.views.decorators.csrf import csrf_exempt

obj = Config()

# Create your views here.
def displayQueries(request):
    return render(request, 'index.html')

@csrf_exempt
def getQ1(request):
    year = request.GET['year']
    data = obj.query1(year)
    context = {}
    if data:
        context['data'] = data
        context['year'] = year
        return render(request, 'query1.html', context)
    else:
        return render(request, 'error.html', context)

@csrf_exempt
def getQ2(request):
    year = request.GET['year_2']
    month = request.GET['month']
    airbase = request.GET['airBase']
    data = obj.query2(year, month, airbase)
    context = {}
    if data:
        context['data'] = data
        context['wsid'] = airbase
        context['year'] = year
        context['month'] = month
        return render(request, 'query2.html', context)
    else:
        return render(request, 'error.html', context)

@csrf_exempt
def getQ3(request):
    year = request.GET['year_3']
    station = request.GET['station']
    data = obj.query3(year, station)
    context = {}
    if data:
        context['data'] = data
        context['wsid'] = station
        context['year'] = year
        return render(request, 'query3.html', context)
    else:
        return render(request, 'error.html', context)