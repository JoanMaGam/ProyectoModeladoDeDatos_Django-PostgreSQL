from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee, Country, Location, Place, Job, Salary


# Create your views here.

def gestion(request):
    return HttpResponse('funciona!')
