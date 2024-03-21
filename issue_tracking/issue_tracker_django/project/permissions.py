from rest_framework import permissions


class ProjectPermissions(permissions.BasePermission):
    def has_permission(self,request,view):
        if request.user.is_authenticated:
            print('stop hererasdas?')
            return True
    def has_object_permission(self,request,view,obj):#it stops here
        if request.user.is_superuser:
            return True
        if request.user.has_perm('project.add_project'):
            return True
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        if request.user.is_staff:
            return True
        return False