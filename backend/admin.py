from django.contrib import admin
from .models import PatientDemographics, VitalSigns, DoctorNote

# Register the models with the Django admin site
admin.site.register(PatientDemographics)
admin.site.register(VitalSigns)
admin.site.register(DoctorNote)

