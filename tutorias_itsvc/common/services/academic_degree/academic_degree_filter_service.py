from tutorias_itsvc.common.repositories import AcademicDegreeRepository


class AcademicDegreeFilterService:
    def __init__(self, repository: AcademicDegreeRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
