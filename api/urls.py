# In api/urls.py

from django.urls import path
from .views import (
    EquipmentListView,
    EquipmentDetailView,
    PersonnelListView,
    PersonnelDetailView,
    JobListView,
    JobDetailView,
    MaintenanceLogListView,
    UserDetailView,
    health_check,
)

urlpatterns = [
    path('equipment/', EquipmentListView.as_view(), name='equipment-list'),
    path('equipment/<int:pk>/', EquipmentDetailView.as_view(), name='equipment-detail'),
    path('personnel/', PersonnelListView.as_view(), name='personnel-list'),
    path('personnel/<int:pk>/', PersonnelDetailView.as_view(), name='personnel-detail'),
    path('jobs/', JobListView.as_view(), name='job-list'),
    path('jobs/<int:pk>/', JobDetailView.as_view(), name='job-detail'),
    path('maintenance/', MaintenanceLogListView.as_view(), name='maintenance-list'),
    path('users/me/', UserDetailView.as_view(), name='user-detail'),
    path('health/', health_check, name='health-check'), # <-- Add this line
]
