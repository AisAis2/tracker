from rest_framework import permissions

class contribAuthPermissions(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated:
            return self.has_object_permission(request,view)
    def has_object_permission(self,request,view):
        if request.user.is_superuser:
            return True
        if request.user.groups.get().name =='admin':
            return True
        return False