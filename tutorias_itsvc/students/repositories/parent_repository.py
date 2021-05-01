from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentParent


class ParentRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentParent
        super(ParentRepository, self).__init__(model)
