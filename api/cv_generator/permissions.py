from django import Request
from rest_framework import permissions

from .models import UserProfile


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view, obj: UserProfile):
        return obj.user == request.user
