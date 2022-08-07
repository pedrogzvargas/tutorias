from tutorias_itsvc.users.repositories import PersonalInformationRepository


class PersonalInformationDeleterService:
    def __init__(self, repository: PersonalInformationRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
