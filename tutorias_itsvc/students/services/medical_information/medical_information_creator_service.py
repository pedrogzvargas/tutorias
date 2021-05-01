from tutorias_itsvc.students.repositories import MedicalInformationRepository


class MedicalInformationCreatorService:
    def __init__(self, repository: MedicalInformationRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
