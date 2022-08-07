from tutorias_itsvc.common.repositories import HousingTypeRepository


class HousingTypeGetterService:
    def __init__(self, repository: HousingTypeRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
