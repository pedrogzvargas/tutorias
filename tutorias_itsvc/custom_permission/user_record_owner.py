from rest_framework.permissions import BasePermission


class UserRecordOwner(BasePermission):
    """
    Allows access only to record owner.
    """

    def has_permission(self, request, view):
        user_id = view.kwargs.get("user_id")
        return bool(request.user.id == user_id)
