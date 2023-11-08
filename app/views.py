from django.shortcuts import render

# Create your views here. 
from django.http import HttpResponse 

def jamPandu(request):
    return HttpResponse('Hai JamPandu How Are U'),
