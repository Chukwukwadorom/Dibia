from rest_framework import generics
from .documents import DoctorNoteDocument
from .models import PatientDemographics, VitalSigns, DoctorNote 
from .serializers import PatientDemographicsSerializer, VitalSignsSerializer, DoctorNoteSerializer, DoctorNoteDocumentSerializer
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    CompoundSearchFilterBackend,
)
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer

class PatientDemographicsListCreateView(generics.ListCreateAPIView):
    queryset = PatientDemographics.objects.all()
    serializer_class = PatientDemographicsSerializer

class PatientDemographicsRetrieveView(generics.RetrieveAPIView):
    queryset = PatientDemographics.objects.all()
    serializer_class = PatientDemographicsSerializer
    lookup_field = 'id'

# PatientDemographics_as_view = PatientDemographicsListCreateView.as_view()

class VitalSignsListCreateView(generics.ListCreateAPIView):
    queryset = VitalSigns.objects.all()
    serializer_class = VitalSignsSerializer


class DoctorNoteListCreateView(generics.ListCreateAPIView):
    queryset = DoctorNote.objects.all()
    serializer_class = DoctorNoteSerializer


class DoctorNoteSearchView(DocumentViewSet):
    document = DoctorNoteDocument
    serializer_class = DoctorNoteDocumentSerializer
    pagination_class = PageNumberPagination
    filter_backends = [
        FilteringFilterBackend,
        CompoundSearchFilterBackend,
    ]
    search_fields = ('note', 'patient_id')
    filter_fields = {
        'patient_id': 'patient_id.keyword',  # Filter on exact patient ID
    }

    def get_queryset(self):
        return DoctorNoteDocument.search()
    