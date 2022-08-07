from tutorias_itsvc.users.repositories import PersonPhoneRepository


class PersonPhoneUpdaterService:
    def __init__(self, repository: PersonPhoneRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
