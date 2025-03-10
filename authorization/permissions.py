from rest_framework import permissions

class IsStaffOrSuperUser(permissions.IsAdminUser):

    def has_permission(self, request, view):
        return bool(super().has_permission(request,view) and request.user.is_superuser)
