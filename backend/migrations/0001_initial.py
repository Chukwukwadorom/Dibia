# Generated by Django 4.2.16 on 2024-11-10 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PatientDemographics",
            fields=[
                (
                    "patient_id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("date", models.DateField()),
                ("age", models.PositiveIntegerField()),
                ("sex", models.CharField(max_length=10)),
                ("occupation", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "marital_status",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("address", models.TextField(blank=True, null=True)),
                ("religion", models.CharField(blank=True, max_length=50, null=True)),
                ("tribe", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="VitalSigns",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("blood_pressure", models.CharField(max_length=20)),
                ("temperature", models.DecimalField(decimal_places=1, max_digits=4)),
                ("respiratory_rate", models.PositiveIntegerField()),
                ("pulse_rate", models.PositiveIntegerField()),
                (
                    "patient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="vital_signs",
                        to="backend.patientdemographics",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DoctorNote",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("note", models.TextField()),
                (
                    "patient_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="doctor_notes",
                        to="backend.patientdemographics",
                    ),
                ),
            ],
        ),
    ]
