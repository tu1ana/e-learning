from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsModerator(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        return False


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class IsStudent(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.student:
            return True
        return False


class IsStudentOrStaff(BasePermission):

    # def has_permission(self, request, view):
    #     if view.action in ['create', 'destroy']:
    #         return request.user.is_superuser
    #     elif view.action in ['update', 'partial_update', 'retrieve', 'list']:
    #         return request.user.is_staff
    #     else:
    #         return False

    # def has_object_permission(self, request, view, obj):
    #     if view.action in ['retrieve', 'update', 'partial_update']:
    #         return request.user == obj.student
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.owner == request.user
