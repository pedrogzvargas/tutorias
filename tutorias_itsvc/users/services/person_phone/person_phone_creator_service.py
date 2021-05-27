from tutorias_itsvc.users.repositories import PersonPhoneRepository


class PersonPhoneCreatorService:
    def __init__(self, repository: PersonPhoneRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
