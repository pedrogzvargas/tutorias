from tutorias_itsvc.common.repositories import AcademicDegreeRepository


class AcademicDegreeGetterService:
    def __init__(self, repository: AcademicDegreeRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
