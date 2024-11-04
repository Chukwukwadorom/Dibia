from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientDemographicsListCreateView

router = DefaultRouter()
# router.register(r'yourmodel', YourModelViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path("", PatientDemographicsListCreateView.as_view(), name="patient-demographics")
]
