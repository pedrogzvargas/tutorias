from tutorias_itsvc.academy.repositories import AcademicMajorRepository


class AcademicMajorFilterService:
    def __init__(self, repository: AcademicMajorRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
