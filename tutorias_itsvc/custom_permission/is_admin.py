from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """
    Allows access only if is tutor.
    """

    def has_permission(self, request, view):
        allowed = False
        if request.user.groups.filter(name="admin"):
            allowed = True
        return allowed
