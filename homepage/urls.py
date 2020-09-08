from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('.well-known/acme-challenge/abw8FqLu00iukYlfDPGichgYlisQINKiydEhyBPnieg', views.certificate, name='certificate'),
]