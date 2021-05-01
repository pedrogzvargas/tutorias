from tutorias_itsvc.users.repositories import PersonalInformationRepository


class PersonalInformationGetterService:
    def __init__(self, repository: PersonalInformationRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
