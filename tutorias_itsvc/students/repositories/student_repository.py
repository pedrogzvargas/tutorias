from shared.repositories import Repository
from tutorias_itsvc.students.models import Student


class StudentRepository(Repository):
    def __init__(self, model=None):
        model = model or Student
        super(StudentRepository, self).__init__(model)
