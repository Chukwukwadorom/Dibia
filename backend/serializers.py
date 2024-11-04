from rest_framework import serializers
from .models import PatientDemographics, VitalSigns

class PatientDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDemographics
        fields = '__all__'

class VitalSignsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VitalSigns
        fields = '__all__'
