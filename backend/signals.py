from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DoctorNote
from .documents import DoctorNoteDocument  # Import the Elasticsearch Document

@receiver(post_save, sender=DoctorNote)
def update_doctor_note_document(sender, instance, **kwargs):
    # Update the Elasticsearch index for this note
    DoctorNoteDocument().update(instance)
