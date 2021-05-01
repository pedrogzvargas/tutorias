from tutorias_itsvc.students.repositories import MedicalInformationRepository


class MedicalInformationUpdaterService:
    def __init__(self, repository: MedicalInformationRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
