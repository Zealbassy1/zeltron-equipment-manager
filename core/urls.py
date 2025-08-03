# In core/urls.py

from django.contrib import admin
from django.urls import path, include
# Import the special views from the simplejwt library
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

    # --- THIS IS THE CORRECTED SECTION ---
    # The path is now /api/token/ which matches your frontend
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]