from tutorias_itsvc.students.repositories import CaracteristicasPersonalesRepository


class CaracteristicasPersonalesGetterService:
    def __init__(self, repository: CaracteristicasPersonalesRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
