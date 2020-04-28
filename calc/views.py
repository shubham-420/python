from django.shortcuts import render
# from django.http import HttpResponse 
from .models import Result
# Create your views here.


def home(request):
    return render(request, 'home.html', {'name': 'shubham'})




def add(request):
    name = request.POST['birthday']
    return render (request, 'result.html', {'ans': name})