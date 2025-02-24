from django.db import models

class PatientDemographics(models.Model):
    patient_id = models.CharField(max_length=100, primary_key=True)
    date = models.DateField()
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=10)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    marital_status = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    religion = models.CharField(max_length=50, blank=True, null=True)
    tribe = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Patient ID: {self.patient_id}"

class VitalSigns(models.Model):
    patient = models.ForeignKey(PatientDemographics, related_name='vital_signs', on_delete=models.CASCADE)
    date = models.DateField()
    blood_pressure = models.CharField(max_length=20)  
    temperature = models.DecimalField(max_digits=4, decimal_places=1) 
    respiratory_rate = models.PositiveIntegerField()
    pulse_rate = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.patient.patient_id} - {self.date}"

class DoctorNote(models.Model):
    patient = models.ForeignKey(PatientDemographics, related_name='doctor_notes', on_delete=models.CASCADE)
    date = models.DateField()
    note = models.TextField()  

    def __str__(self):
        return f"Doctor Note for {self.patient.patient_id} on {self.date}"
