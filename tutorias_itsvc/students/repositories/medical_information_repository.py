from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentMedicalInformation


class MedicalInformationRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentMedicalInformation
        super(MedicalInformationRepository, self).__init__(model)
