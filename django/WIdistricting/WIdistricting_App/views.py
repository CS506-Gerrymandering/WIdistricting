from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers

from WIdistricting_App.models import District, District_Plan


def index(request):
    return HttpResponse("home page")

def get_districts(request):
    return HttpResponse("I work")

def get_district_plans(request):
    return HttpResponse("district plans")

def get_all_district_metrics(request):
    response = serializers.serialize('json', District.objects.all())
    return HttpResponse(response)

def get_statewide_metrics(request):
    response = serializers.serialize('json', District_Plan.objects.all())
    return HttpResponse(response)
