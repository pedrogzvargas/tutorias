from tutorias_itsvc.users.repositories import PersonalInformationRepository


class PersonalInformationUpdaterService:
    def __init__(self, repository: PersonalInformationRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
