from rest_framework import serializers
from medicines.models import Medicine
from research_facilities.models import ResearchFacility

'''
There are 2 ways to generate the Serializer, below they are explain
'''

#1. Automatic Model, we must incude the Meta class to define the model in which the Serializer is going to be generated
class ResearschFacilitySerializer(serializers.ModelSerializer):
   class Meta:
        model = ResearchFacility
        fields = ['id','name']

class MedicinesSerializerResponse(serializers.Serializer):
        id = serializers.IntegerField(read_only=True)
        name = serializers.CharField()
        price = serializers.IntegerField()
        research_facility_id = serializers.IntegerField()
        ResearchFacility = ResearschFacilitySerializer(read_only=True) #20240417 Pending this functionality as the Serializers is not printing the relationship


class MedicineSerializerRequest(serializers.Serializer):
        name = serializers.CharField()
        price = serializers.IntegerField()

'''
#2. Field by field Model
class MedicinesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.IntegerField()
    #price_format = serializers.CharField()
    research_facility_id = serializers.IntegerField()


    def create(self, name, price, research_facility_id):
        return Medicine.objects.create(
            name=name,
            price=price,
            research_facility_id=research_facility_id
        )
        
           # With the above method we can create a new medicament
           # {
           #     "name": "Omeprazole",
           #     "price": 35,
           #     "research_facility_id": 2
           # }

    
'''



