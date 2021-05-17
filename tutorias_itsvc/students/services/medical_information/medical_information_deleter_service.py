from tutorias_itsvc.students.repositories import MedicalInformationRepository


class MedicalInformationDeleterService:
    def __init__(self, repository: MedicalInformationRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
