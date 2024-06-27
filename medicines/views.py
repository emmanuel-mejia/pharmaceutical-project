from medicines.models import Medicine
from medicines.serializers import MedicinesSerializerResponse
from medicines.serializers import MedicineSerializerRequest
from rest_framework.response import Response #JSON response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    medicines = Medicine.objects.all()#modelo traer objeto y a la función all
    #return HttpResponse('Hello Pharmaceutical Company')
    return render(request, 'index.html',{'medicines':medicines})

@api_view(['GET','POST'])
def medicines(request):

    if request.method == 'GET':

        medicines = Medicine.objects.all()
        serializer_medicines = MedicinesSerializerResponse(medicines, many=True)

        return Response(serializer_medicines.data)
    
    else: 
        
        #A new serializer is generated from the entered data
        #{"name":"Paracetamol", "price_format":25}

        #Only the included values will be taken into consideration
        #{"name":"Paracetamol", "price_format":25,"Hack attempt":"Hack attempt"} 
        
        serializer_medicines = MedicinesSerializerResponse(data=request.data)

        if serializer_medicines.is_valid():
        
            Medicine.objects.create(
                name=request.data['name'],
                price=request.data['price'],
                research_facility_id=request.data['research_facility_id']
            )
            #print(serializer_medicines.data)
            return Response(serializer_medicines.data)
    

            '''
            #Other way to do this is by obtaining and parse the data 
            serializer_medicines.create(
                request.data['name'],
                request.data['price'],
                request.data['research_facility_id']
            )
            '''


@api_view(['GET', 'PUT', 'DELETE'])
def detail_medicine(request, pk):

    medicine = Medicine.objects.get(pk=pk)

    if request.method == 'GET':
        pass
    
    if request.method == 'PUT':

        serializer = MedicineSerializerRequest(data=request.data) #Serialize

        if serializer.is_valid():#Validation
            medicine.name = request.data['name']#persistance
            medicine.price = request.data['price']
            medicine.save() #saving

    if request.method == 'DELETE':
        
            medicine.delete()
            medicine.save() #saving

    serializer = MedicinesSerializerResponse(medicine) #return
    return Response(serializer.data)

        


'''
#240416 JsonResponse was changed by the restframework
 
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
