# In api/serializers.py

from rest_framework import serializers
from .models import Equipment, Personnel, Job, MaintenanceLog
from django.contrib.auth.models import User

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'

class PersonnelSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=False)
    email = serializers.EmailField(write_only=True, required=False)
    first_name = serializers.CharField(write_only=True, required=False)
    last_name = serializers.CharField(write_only=True, required=False)
    user_full_name = serializers.CharField(source='user.get_full_name', read_only=True)

    class Meta:
        model = Personnel
        fields = [
            'id', 'user', 'user_full_name', 'role', 'contact_number', 'status',
            'username', 'password', 'email', 'first_name', 'last_name'
        ]
        read_only_fields = ['user']

    def create(self, validated_data):
        user_data = {
            'username': validated_data.pop('username'),
            'email': validated_data.pop('email'),
            'first_name': validated_data.pop('first_name', ''),
            'last_name': validated_data.pop('last_name', ''),
        }
        password = validated_data.pop('password')
        user = User.objects.create_user(**user_data, password=password)
        personnel = Personnel.objects.create(user=user, **validated_data)
        return personnel

class JobEquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = ['id', 'name', 'identifier']

class JobPersonnelSerializer(serializers.ModelSerializer):
    user_full_name = serializers.CharField(source='user.get_full_name', read_only=True)
    class Meta:
        model = Personnel
        fields = ['id', 'user_full_name', 'role']

class JobSerializer(serializers.ModelSerializer):
    equipment = JobEquipmentSerializer(many=True, read_only=True)
    personnel = JobPersonnelSerializer(many=True, read_only=True)
    equipment_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Equipment.objects.all(), source='equipment'
    )
    personnel_ids = serializers.PrimaryKeyRelatedField(
        many=True, write_only=True, queryset=Personnel.objects.all(), source='personnel'
    )

    class Meta:
        model = Job
        fields = [
            'id', 'job_name', 'site_location', 'equipment', 'personnel',
            'deployment_date', 'return_date', 'status',
            'equipment_ids', 'personnel_ids'
        ]

class MaintenanceLogSerializer(serializers.ModelSerializer):
    equipment_name = serializers.StringRelatedField(source='equipment')
    mechanic_name = serializers.StringRelatedField(source='mechanic')

    class Meta:
        model = MaintenanceLog
        fields = [
            'id', 'equipment', 'equipment_name', 'mechanic', 'mechanic_name',
            'service_date', 'service_type', 'notes', 'cost', 'generated_summary'
        ]

class UserSerializer(serializers.ModelSerializer):
    personnel = PersonnelSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'personnel']
