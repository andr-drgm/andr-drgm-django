from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'homepage/homepage.html', {})

def certificate(request):
    return HttpResponse("gaHo22OCDjGul00lQC68n-APKBhyw3vBBTuYyTQ-LFU.a2-S4sebDylkm7AjvFbUUnyTLPiz0Fnx4l0nshSa0YQ")