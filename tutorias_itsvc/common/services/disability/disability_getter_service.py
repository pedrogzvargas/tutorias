from tutorias_itsvc.common.repositories import DisabilityRepository


class DisabilityGetterService:
    def __init__(self, repository: DisabilityRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
