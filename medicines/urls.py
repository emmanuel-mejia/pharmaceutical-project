from django.contrib import admin
from django.urls import path

from medicines.views import medicines
from medicines.views import detail_medicine
from medicines.views import index

urlpatterns = [
    path('', index, name='index'),
    path('', medicines),
    path('/<int:pk>', detail_medicine) #Everything is going to be treated as a PK
]