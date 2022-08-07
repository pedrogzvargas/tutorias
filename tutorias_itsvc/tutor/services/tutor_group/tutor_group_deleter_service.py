from tutorias_itsvc.tutor.repositories import TutorGroupRepository


class TutorGroupDeleterService:
    def __init__(self, repository: TutorGroupRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
