from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return render(request, 'homepage/homepage.html', {})

def certificate(request):
    return HttpResponse("muPYUH_8KW7eAFCZWePd2GOIDMUpVqCuiW3OySfES7s.a2-S4sebDylkm7AjvFbUUnyTLPiz0Fnx4l0nshSa0YQ")