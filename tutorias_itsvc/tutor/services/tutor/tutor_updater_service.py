from tutorias_itsvc.tutor.repositories import TutorRepository


class TutorUpdaterService:
    def __init__(self, repository: TutorRepository):
        self.__repository = repository

    def __call__(self, id,  **kwargs):
        return self.__repository.update(id, **kwargs)
