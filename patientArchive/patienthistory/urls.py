from django.urls import path
from . import views

urlpatterns = [
    path('', views.patientList, name='patientList'),
    path('searchID/', views.searchPatientById, name='searchPatientById'),
    path('searchName/', views.searchPatientByName, name='searchPatientByName'),
    path('add/', views.addPatient, name='addPatient'),
    path('<PatientId>/addVisit', views.patientHistadd, name='patientHistadd'),
]
