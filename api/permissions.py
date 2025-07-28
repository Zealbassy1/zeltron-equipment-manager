# In api/permissions.py

from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    """
    Custom permission to only allow users with the 'admin' or 'manager' role.
    """

    def has_permission(self, request, view):
        # First, check if the user is logged in and has a personnel profile.
        # The `hasattr` check is important to prevent errors if a user somehow
        # doesn't have a profile linked.
        if not request.user or not hasattr(request.user, 'personnel'):
            return False

        # Then, check if their role is one of the allowed roles.
        return request.user.personnel.role in ['admin', 'manager']