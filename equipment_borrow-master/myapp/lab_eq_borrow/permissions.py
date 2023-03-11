from rest_framework.permissions import BasePermission

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='user').exists()


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()


class CanViewItems(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='user').exists() or request.user.groups.filter(name='admin').exists()

class CanViewItemDetails(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='user').exists() or request.user.groups.filter(name='admin').exists()

class CanAddItem(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()

class CanEditItem(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()

class CanDeleteItem(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='admin').exists()