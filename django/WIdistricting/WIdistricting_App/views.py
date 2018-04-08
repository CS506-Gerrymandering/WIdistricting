from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("home page")

def get_districts(request):
    return HttpResponse("I work")
