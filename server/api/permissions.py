from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrReadOnly(BasePermission):
    """
    Custom permission to allow only admin users to edit (POST, PUT, PATCH, DELETE) objects.
    Allows anyone to view (GET) objects.
    """

    def has_permission(self, request, view):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        return request.user and request.user.is_staff

class AllowPostOnly(BasePermission):
    """
    Custom permission to allow only POST requests from anyone.
    Only admin users can GET, PUT, PATCH, DELETE.
    """

    def has_permission(self, request, view):
        if request.method == 'POST':
            return True
        return request.user and request.user.is_staff if request.user else False

class AdminOnlyPermission(BasePermission):
    """
    Custom permission to allow only admin users to perform all actions (GET, POST, PUT, PATCH, DELETE).
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class AllowPostAndGetOnly(BasePermission):
    """
    Custom permission to allow both POST and GET requests from any user.
    Only admin users can PUT, PATCH, DELETE.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS or request.method == 'POST':
            return True
        return request.user and request.user.is_staff if request.user else False