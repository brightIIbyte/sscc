from django.shortcuts import render
from .models import SSCC

def generate_sscc(request):
    extension_digit = 1
    gs1_prefix = "123456789"
    serial_reference_number = "9876543"

    sscc = SSCC(extension_digit=extension_digit, gs1_prefix=gs1_prefix, serial_reference_number=serial_reference_number)
    sscc.save()

    context = {
        'sscc': sscc,
    }

    return render(request, 'sscc/generate_sscc.html', context)