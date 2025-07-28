# In api/views.py

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from .models import Equipment, Personnel, Job, MaintenanceLog
from .serializers import (
    EquipmentSerializer, PersonnelSerializer, JobSerializer, 
    MaintenanceLogSerializer, UserSerializer
)
from .permissions import IsAdminOrManager
from django.http import JsonResponse

class EquipmentListView(generics.ListCreateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrManager()]
        return super().get_permissions()

class EquipmentDetailView(generics.RetrieveUpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminOrManager]

class PersonnelListView(generics.ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAdminOrManager]

class PersonnelDetailView(generics.RetrieveUpdateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAdminOrManager]

class JobListView(generics.ListCreateAPIView):
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, 'personnel') and user.personnel.role in ['admin', 'manager']:
            return Job.objects.all().order_by('-deployment_date')
        if hasattr(user, 'personnel'):
            return Job.objects.filter(personnel=user.personnel).order_by('-deployment_date')
        return Job.objects.none()

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminOrManager()]
        return super().get_permissions()

    def perform_create(self, serializer):
        job = serializer.save()
        equipment_ids = self.request.data.get('equipment_ids', [])
        Equipment.objects.filter(id__in=equipment_ids).update(status='deployed')

class JobDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAdminOrManager]

    def perform_update(self, serializer):
        job = serializer.instance
        new_status = self.request.data.get('status')
        if new_status == 'completed' and job.status == 'active':
            equipment_ids = [e.id for e in job.equipment.all()]
            Equipment.objects.filter(id__in=equipment_ids).update(status='available')
        serializer.save()

class MaintenanceLogListView(generics.ListCreateAPIView):
    queryset = MaintenanceLog.objects.all().order_by('-service_date')
    serializer_class = MaintenanceLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
         if self.request.method == 'POST':
            return [IsAdminOrManager()]
         return super().get_permissions()

class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
def health_check(request):
    """A simple, public endpoint for the load balancer to check."""
    return JsonResponse({"status": "ok"})