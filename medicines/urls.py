from django.contrib import admin
from django.urls import path

from medicines.views import medicines

urlpatterns = [
    path('', medicines),
]