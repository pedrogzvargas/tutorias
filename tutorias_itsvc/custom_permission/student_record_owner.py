from rest_framework.permissions import BasePermission


class StudentRecordOwner(BasePermission):
    """
    Allows access only to record owner.
    """

    def has_permission(self, request, view):
        student_id = view.kwargs.get("student_id")
        allowed = False
        if hasattr(request.user, 'student'):
            allowed = bool(request.user.student.id == student_id)
        return allowed
