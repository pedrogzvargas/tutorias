from tutorias_itsvc.users.repositories import PersonPhoneRepository


class PersonPhoneFilterService:
    def __init__(self, repository: PersonPhoneRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
