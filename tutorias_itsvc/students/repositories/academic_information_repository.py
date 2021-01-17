from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentAcademicInformation


class AcademicInformationRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentAcademicInformation
        super(AcademicInformationRepository, self).__init__(model)
