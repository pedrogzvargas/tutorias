from tutorias_itsvc.tutor.repositories import TutorSubjectRepository


class TutorSubjectUpdaterService:
    def __init__(self, repository: TutorSubjectRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
