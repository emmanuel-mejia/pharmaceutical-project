from django.shortcuts import render
from django.http import JsonResponse
from medicines.models import medicine

def medicines(request):
    #print('Path medicines')
    #return 'Path medicines'
    #JSON
    medicines = medicine.objects.all()
    return JsonResponse(medicines)