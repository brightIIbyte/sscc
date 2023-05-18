from django.urls import path
from .views import generate_sscc

app_name = 'sscc'

urlpatterns = [
    path('generate/', generate_sscc, name='generate_sscc'),
]