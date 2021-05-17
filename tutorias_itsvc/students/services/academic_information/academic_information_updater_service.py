from tutorias_itsvc.students.repositories import AcademicInformationRepository


class AcademicInformationUpdaterService:
    def __init__(self, repository: AcademicInformationRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.update(**kwargs)
