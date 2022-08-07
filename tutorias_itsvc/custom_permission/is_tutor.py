from rest_framework.permissions import BasePermission


class IsTutor(BasePermission):
    """
    Allows access only if is tutor.
    """

    def has_permission(self, request, view):
        allowed = False
        if request.user.groups.filter(name="tutor"):
            allowed = True
        return allowed
