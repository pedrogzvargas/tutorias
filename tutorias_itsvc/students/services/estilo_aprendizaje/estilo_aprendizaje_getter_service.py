from tutorias_itsvc.students.repositories import EstiloAprendizajeRepository


class EstiloAprendizajeGetterService:
    def __init__(self, repository: EstiloAprendizajeRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
