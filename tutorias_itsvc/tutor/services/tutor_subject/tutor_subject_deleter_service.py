from tutorias_itsvc.tutor.repositories import TutorSubjectRepository


class TutorSubjectDeleterService:
    def __init__(self, repository: TutorSubjectRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
