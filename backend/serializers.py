from rest_framework import serializers
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from .models import PatientDemographics, VitalSigns, DoctorNote
from .documents import DoctorNoteDocument

class PatientDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDemographics
        fields = '__all__'

class VitalSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSigns
        fields = '__all__'


class DoctorNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorNote
        fields = '__all__'


class DoctorNoteDocumentSerializer(DocumentSerializer):
    class Meta:
        document = DoctorNoteDocument
        fields = (
            'patient_id',
            'note',
            'date',
        )
