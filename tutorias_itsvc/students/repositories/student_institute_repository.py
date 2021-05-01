from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentInstitute


class StudentInstituteRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentInstitute
        super(StudentInstituteRepository, self).__init__(model)
