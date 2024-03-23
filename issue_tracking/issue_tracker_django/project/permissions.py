from rest_framework import permissions


class ProjectPermissions(permissions.BasePermission):
    def has_permission(self,request,view):
        if not request.user.is_authenticated:
            return False
        return self.has_object_permission(request,view)
    def has_object_permission(self,request,view):#it stops here
        if request.user.is_superuser:
            return True
        if request.user.has_perm('project.add_project') and request.method =='POST':
            return True
        # if request.method in permissions.SAFE_METHODS:# add case when methods is unsafe return false
        #     return True

        if request.user.has_perm('project.edit_project') and request.method =='PUT':
            return True
        if request.user.has_perm('project.delete_project') and request.method == 'DELETE':
            return True
        if request.user.is_staff:
            return True
        return False
class TicketPermissions(permissions.BasePermission):
    def has_permission(self,request,view):
        if not request.user.is_authenticated:
            return False
        return self.has_object_permission(request,view,request.data)
    def has_object_permission(self,request,view,obj):
        if request.user.is_superuser:
            return True
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        if request.user.has_perm('ticket.add_ticket') and request.method =='POST':
            return True
        if request.user.has_perm('ticket.change_ticket') and request.method =='PUT': #and obj['submitter']['id']== request.user.id:#how to pass ticket object? I pass request[] obj, serializer required? 
            return True
        if request.user.is_staff:
            return True
        return False