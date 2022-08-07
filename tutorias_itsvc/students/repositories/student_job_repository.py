from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentJob


class StudentJobRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentJob
        super(StudentJobRepository, self).__init__(model)
