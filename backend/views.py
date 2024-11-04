from rest_framework import generics
from .models import PatientDemographics, VitalSigns
from .serializers import PatientDemographicsSerializer, VitalSignsSerializer

class PatientDemographicsListCreateView(generics.ListCreateAPIView):
    queryset = PatientDemographics.objects.all()
    serializer_class = PatientDemographicsSerializer

# PatientDemographics_as_view = PatientDemographicsListCreateView.as_view()

class VitalSignsListCreateView(generics.ListCreateAPIView):
    queryset = VitalSigns.objects.all()
    serializer_class = VitalSignsSerializer
