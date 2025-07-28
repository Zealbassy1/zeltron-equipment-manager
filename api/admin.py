from django.contrib import admin
from .models import Equipment, Personnel, Job, MaintenanceLog # Import our personnel models

# Register your models here.
# In api/admin.py
from .models import Equipment  # Import our Equipment model

# Register your models here.
admin.site.register(Equipment) # This tells Django to show the Equipment model in the admin site
admin.site.register(Personnel)
admin.site.register(Job)
admin.site.register(MaintenanceLog)  # Register the MaintenanceLog model