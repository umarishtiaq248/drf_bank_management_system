from rest_framework import permissions


class SelfUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
