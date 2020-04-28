from django.shortcuts import render
# from django.http import HttpResponse 
from .models import Result
# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'shubham'})

def add(request):
    result = "weather is good"
    return render (request, 'result.html', {'result': result})

