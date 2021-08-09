from tutorias_itsvc.tutor.repositories import TutorRepository


class TutorCreatorService:
    def __init__(self, repository: TutorRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
