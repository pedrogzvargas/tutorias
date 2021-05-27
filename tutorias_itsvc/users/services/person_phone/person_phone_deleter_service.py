from tutorias_itsvc.users.repositories import PersonPhoneRepository


class PersonPhoneDeleterService:
    def __init__(self, repository: PersonPhoneRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
