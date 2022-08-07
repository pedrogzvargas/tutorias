from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentSibling


class StudentSiblingRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentSibling
        super(StudentSiblingRepository, self).__init__(model)
