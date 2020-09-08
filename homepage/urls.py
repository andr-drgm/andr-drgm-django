from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('.well-known/acme-challenge/g4cmTro7oBBmSUUbe4Y9VT42s3nShL1Cs9QJF0T4Fm4', views.certificate, name='certificate'),
]