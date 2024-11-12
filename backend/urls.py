from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientDemographicsListCreateView, PatientDemographicsRetrieveView,VitalSignsListCreateView, DoctorNoteSearchView, DoctorNoteListCreateView

router = DefaultRouter()
# router.register(r'yourmodel', YourModelViewSet)

urlpatterns = [
    path('patients/', PatientDemographicsListCreateView.as_view(), name='patient-demographics'),
    path('patientdemographics/<int:id>/', PatientDemographicsRetrieveView.as_view(), name='patientdemographics-retrieve'),
    path('vitals/', VitalSignsListCreateView.as_view(), name='vital-signs'),
    path('doctornotes/', DoctorNoteListCreateView.as_view(), name='doctornote-create'),
    path('doctornotes/search/', DoctorNoteSearchView.as_view({'get': 'list'}), name='doctor-note-search'),
]