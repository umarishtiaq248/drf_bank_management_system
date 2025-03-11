from rest_framework import permissions


class IsStaffOrSuperUser(permissions.IsAdminUser):
  
    def has_permission(self, request, view):
        return bool(super().has_permission(request,view) and request.user.is_superuser)
      

class SelfUser(permissions.BasePermission):
  
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

