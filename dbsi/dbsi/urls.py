"""dbsi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

from redisapp import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls), 
    re_path(r'^highschooldirectory', views.loadHomePage),
    path('q1Data', views.getQ1, name='getQ1'),
    path('q2Data', views.getQ2, name='getQ2'),
    path('q3Data', views.getQ3, name='getQ3'),
    path('q4Data', views.getQ4, name='getQ4'),
    path('database', views.getQ5, name='database')
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

