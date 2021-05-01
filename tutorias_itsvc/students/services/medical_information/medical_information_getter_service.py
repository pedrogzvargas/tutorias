from tutorias_itsvc.students.repositories import MedicalInformationRepository


class MedicalInformationGetterService:
    def __init__(self, repository: MedicalInformationRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
