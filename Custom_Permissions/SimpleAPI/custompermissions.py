# Custome_Permissions With your choice.
# Two ways
# def has_permissions(self, request, view)
# def has_object_permissions(self, request, view, obj)


from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return False
