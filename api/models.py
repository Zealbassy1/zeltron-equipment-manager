# In api/models.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('deployed', 'Deployed'),
        ('maintenance', 'Under Maintenance'),
    ]
    TYPE_CHOICES = [
        ('bulldozer', 'Bulldozer'),
        ('excavator', 'Excavator'),
        ('payloader', 'Payloader'),
        ('crane', 'Crane'),
        ('backhoe', 'Backhoe'),
        ('truck' , 'Truck')
    ]
    name = models.CharField(max_length=100)
    identifier = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    last_service_date = models.DateField(null=True, blank=True)
    purchase_date = models.DateField(null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.name} ({self.identifier})"

class Personnel(models.Model):
    ROLE_CHOICES = [
        ('driver', 'Driver'),
        ('operator', 'Operator'),
        ('mechanic', 'Mechanic'),
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    ]
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('on_leave', 'On Leave'),
        ('inactive', 'Inactive'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    contact_number = models.CharField(max_length=20, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    
    def __str__(self):
        # This will show the user's full name and their role in the admin panel.
        full_name = self.user.get_full_name()
        return f"{full_name or self.user.username} ({self.get_role_display()})"

class Job(models.Model):
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('completed', 'Completed'),
    ]
    job_name = models.CharField(max_length=100)
    site_location = models.CharField(max_length=200)
    equipment = models.ManyToManyField(Equipment)
    personnel = models.ManyToManyField(Personnel)
    deployment_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return f"{self.job_name}"

class MaintenanceLog(models.Model):
    SERVICE_TYPE_CHOICES = [
        ('routine_check', 'Routine Check'),
        ('oil_change', 'Oil Change'),
        ('engine_repair', 'Engine Repair'),
        ('hydraulic_fix', 'Hydraulic System Fix'),
        ('other', 'Other'),
    ]
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='maintenance_logs')
    # The limit_choices_to parameter has been removed to ensure compatibility.
    mechanic = models.ForeignKey(Personnel, on_delete=models.PROTECT)
    service_date = models.DateField()
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
    notes = models.TextField()
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    generated_summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Service for {self.equipment.name} on {self.service_date}"
