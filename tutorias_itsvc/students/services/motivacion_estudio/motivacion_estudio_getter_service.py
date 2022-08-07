from tutorias_itsvc.students.repositories import MotivacionEstudioRepository


class MotivacionEstudioGetterService:
    def __init__(self, repository: MotivacionEstudioRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
