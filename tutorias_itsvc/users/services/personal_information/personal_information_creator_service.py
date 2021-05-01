from tutorias_itsvc.users.repositories import PersonalInformationRepository


class PersonalInformationCreatorService:
    def __init__(self, repository: PersonalInformationRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
