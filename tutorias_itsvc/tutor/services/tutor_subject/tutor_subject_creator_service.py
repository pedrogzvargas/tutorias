from tutorias_itsvc.tutor.repositories import TutorSubjectRepository


class TutorSubjectCreatorService:
    def __init__(self, repository: TutorSubjectRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
