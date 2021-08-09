from tutorias_itsvc.common.repositories import DisabilityRepository


class DisabilityFilterService:
    def __init__(self, repository: DisabilityRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
