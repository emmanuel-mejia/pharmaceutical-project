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