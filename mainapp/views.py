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
