from tutorias_itsvc.academy.repositories import SubjectTypeRepository


class SubjectTypeGetterService:
    def __init__(self, repository: SubjectTypeRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
