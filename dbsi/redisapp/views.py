from django.shortcuts import render
from django.core.cache import cache

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from .config import Config
from django.views.decorators.csrf import csrf_exempt

obj = Config()

# Create your views here.
def loadHomePage(request):
    return render(request, 'home.html')

@csrf_exempt
def getQ1(request):
    data = obj.q1()
    context = {}
    if data:
        return render(request, 'q1.html', context)
    else:
        return render(request, 'error.html', context)

@csrf_exempt
def getQ2(request):
    data = obj.q2()
    context = {}
    if data:
        return render(request, 'q2.html', context)
    else:
        return render(request, 'error.html', context)

@csrf_exempt
def getQ3(request):
    data = obj.q3()
    context = {}
    if data:
        return render(request, 'q3.html', context)
    else:
        return render(request, 'error.html', context)