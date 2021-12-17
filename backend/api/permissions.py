from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        # if request.method == 'POST':
        #     return request.user.is_authenticated
        # return True
        return (
            request.method == 'POST' and request.user.is_authenticated
            or request.method in SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        # if request.method in SAFE_METHODS or request.user.is_superuser:
        #     return True
        # return request.user == obj.author
        return (
            request.method in SAFE_METHODS
            or request.user.is_superuser
            or request.user == obj.author)
