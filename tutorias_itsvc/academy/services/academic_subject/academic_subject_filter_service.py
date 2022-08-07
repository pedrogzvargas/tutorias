from tutorias_itsvc.academy.repositories import AcademicSubjectRepository


class AcademicSubjectFilterService:
    def __init__(self, repository: AcademicSubjectRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
