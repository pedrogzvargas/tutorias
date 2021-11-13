from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentScholarship


class StudentScholarshipRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentScholarship
        super(StudentScholarshipRepository, self).__init__(model)
