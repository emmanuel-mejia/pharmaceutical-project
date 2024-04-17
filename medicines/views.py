from medicines.models import Medicine

from medicines.serializers import MedicinesSerializer

from rest_framework.response import Response #JSON response
from rest_framework.decorators import api_view

@api_view(['GET'])
def medicines(request):
    medicines = Medicine.objects.all()
    serializer_medicines = MedicinesSerializer(medicines, many=True)

    return Response(serializer_medicines.data)


'''
#240416 Sustituimos el uso de JsonResponse por el restframework
 
from django.shortcuts import render
from django.http import JsonResponse
from medicines.models import Medicine

def medicines(request): #All functions in Python must be with the request parameter 
    
    #print('Path medicines')
    #return 'Path medicines'
   
    #JSON
    medicines = Medicine.objects.all()

    result = []
    for medicine in medicines: 
        m = {
            'id': medicine.id,
            'name': medicine.name,
            'price': medicine.price,
        }
        result.append(m)

    return JsonResponse(
        {
            'data': result #Dict list
        }
    )
'''
