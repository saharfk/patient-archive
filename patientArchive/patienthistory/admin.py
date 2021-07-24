from django.contrib import admin
from .models import Patient, PatientHistory

admin.site.register(Patient)
admin.site.register(PatientHistory)
