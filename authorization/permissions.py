from rest_framework import permissions

class IsStaffOrSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        permission = request.user.is_staff or request.user.is_superuser
        return user and permission
