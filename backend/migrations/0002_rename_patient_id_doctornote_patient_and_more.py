# Generated by Django 4.2.16 on 2024-11-11 11:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="doctornote",
            old_name="patient_id",
            new_name="patient",
        ),
        migrations.RenameField(
            model_name="vitalsigns",
            old_name="patient_id",
            new_name="patient",
        ),
    ]
