from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'homepage/homepage.html', {})

def certificate(request):
    return HttpResponse("g4cmTro7oBBmSUUbe4Y9VT42s3nShL1Cs9QJF0T4Fm4.a2-S4sebDylkm7AjvFbUUnyTLPiz0Fnx4l0nshSa0YQ")