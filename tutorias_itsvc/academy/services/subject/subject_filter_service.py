from tutorias_itsvc.academy.repositories import SubjectRepository


class SubjectFilterService:
    def __init__(self, repository: SubjectRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
