from tutorias_itsvc.students.repositories import EstadoPsicofisiologicoRepository


class EstadoPsicofisiologicoGetterService:
    def __init__(self, repository: EstadoPsicofisiologicoRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
