from django.urls import path
from homepage import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('.well-known/acme-challenge/muPYUH_8KW7eAFCZWePd2GOIDMUpVqCuiW3OySfES7s', views.certificate, name='certificate'),
]