from django.contrib import admin
from django.urls import path, include
from django.views.generic import ListView, DetailView
from patient.models import Patient_TBL
from patient.views import PatientLV,PatientDV
from patient import views

app_name = 'patient'
urlpatterns = [
    #Exmple:/patient/
    path('',PatientLV.as_view(model=Patient_TBL),name='index'),

    #Example:/patient/index/
    path('<int:pk>/',PatientDV.as_view(model=Patient_TBL),name='detail'),

    # Example: /patient/search/
    path('search/', views.SearchFormView.as_view(), name='search'),
]
