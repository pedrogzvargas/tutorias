from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentPhone


class StudentPhoneRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentPhone
        super(StudentPhoneRepository, self).__init__(model)
