from tutorias_itsvc.common.repositories import AttitudeRepository


class AttitudeGetterService:
    def __init__(self, repository: AttitudeRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
