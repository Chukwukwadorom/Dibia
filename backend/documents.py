from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from .models import DoctorNote

@registry.register_document
class DoctorNoteDocument(Document):

    patient_id = fields.KeywordField()

    class Index:
        name = 'doctornotes'

    class Django:
        model = DoctorNote
        fields = [
            'note',  # Full-text search field
            'date'  # To allow date-based searches or filtering
        ]

    def get_queryset(self):
        # Ensure we are using the correct queryset
        return super().get_queryset().select_related('patient_id')
