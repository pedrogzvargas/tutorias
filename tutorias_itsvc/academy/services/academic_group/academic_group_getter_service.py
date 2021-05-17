from tutorias_itsvc.academy.repositories import AcademicGroupRepository


class AcademicGroupGetterService:
    def __init__(self, repository: AcademicGroupRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
