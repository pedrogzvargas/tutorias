from tutorias_itsvc.tutor.repositories import TutorRepository


class TutorDeleterService:
    def __init__(self, repository: TutorRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
