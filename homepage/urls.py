from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('.well-known/acme-challenge/gaHo22OCDjGul00lQC68n-APKBhyw3vBBTuYyTQ-LFU', views.certificate, name='certificate'),
]