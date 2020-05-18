# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'mainapp/Home.html')

def design_report(request):
    return render(request, 'mainapp/DesignReport.html')

def personal_development(request):
    return render(request, 'mainapp/PD.html')

def presentation(request):
    return render(request, 'mainapp/Presentation.html')

def blog(request):
    return render(request, 'mainapp/Blog.html')

def indus(request):
    return render(request, 'mainapp/indus.html')

def bauhaus(request):
    return render(request, 'mainapp/bauhaus.html')

def newtyp(request):
    return render(request, 'mainapp/newtyp.html')

def newyork(request):
    return render(request, 'mainapp/newyork.html')

def russia(request):
    return render(request, 'mainapp/russia.html')

def psa(request):
    return render(request, 'mainapp/Psa.html')

def roles(request):
    return render(request, 'mainapp/roles.html')

def diary(request):
    return render(request, 'mainapp/diary.html')

