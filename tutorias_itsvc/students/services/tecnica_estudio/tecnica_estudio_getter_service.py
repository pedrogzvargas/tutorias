from tutorias_itsvc.students.repositories import TecnicaEstudioRepository


class TecnicaEstudioGetterService:
    def __init__(self, repository: TecnicaEstudioRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
