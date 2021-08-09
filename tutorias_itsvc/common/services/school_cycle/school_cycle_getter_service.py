from tutorias_itsvc.common.repositories import SchoolCycleRepository


class SchoolCycleGetterService:
    def __init__(self, repository: SchoolCycleRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
