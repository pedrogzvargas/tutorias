from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentSubject


class StudentSubjectRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentSubject
        super(StudentSubjectRepository, self).__init__(model)
