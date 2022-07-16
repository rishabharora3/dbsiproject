from django.shortcuts import render
from django.core.cache import cache

# Create your views here.


from django.shortcuts import render
from django.http import HttpResponse
from .config import Config
from django.views.decorators.csrf import csrf_exempt
import pdb

obj = Config()

# Create your views here.


def loadHomePage(request):
    return render(request, 'home.html')


@csrf_exempt
def getQ1(request):
    school_name = request.GET.get('school_name')
    print(school_name)
    data = obj.q1(school_name)
    context = {}
    if data:
        context['data'] = data
        context['school_name'] = school_name
        context['size'] = len(data)
        return render(request, 'q1.html', context)
    else:
        return render(request, 'error.html', context)


@csrf_exempt
def getQ2(request):
    borough = request.GET.get('borough')
    print(borough)
    data = obj.q2(borough)
    context = {}
    if data:
        context['data'] = data
        context['borough'] = borough
        context['size'] = len(data)
        return render(request, 'q2.html', context)
    else:
        return render(request, 'error.html', context)


@csrf_exempt
def getQ3(request):
    school_name = request.GET.get('school_name')
    print(school_name)
    data = obj.q3(school_name)
    context = {}
    if data:
        context['data'] = data
        context['school_name'] = school_name
        return render(request, 'q3.html', context)
    else:
        return render(request, 'error.html', context)


@csrf_exempt
def getQ4(request):
    school_name = request.GET.get('school_name')
    school_address = request.GET.get('school_address')
    print(school_name)
    data = obj.q4(school_name, school_address)
    context = {}
    if data:
        context['data'] = data
        context['school_name'] = school_name
        context['school_address'] = school_address
        return render(request, 'q4.html', context)
    else:
        return render(request, 'error.html', context)

@csrf_exempt
def getQ5(request):
    data = obj.q5()
    context = {}
    if data:
        context['data'] = data
        context['size'] = len(data)
        return render(request, 'database.html', context)
    else:
        return render(request, 'error.html', context)

