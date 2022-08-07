from tutorias_itsvc.students.repositories import AreaIntegracionRepository


class AreaIntegracionGetterService:
    def __init__(self, repository: AreaIntegracionRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
