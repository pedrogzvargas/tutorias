from tutorias_itsvc.academy.repositories import AcademicPeriodRepository


class AcademicPeriodFilterService:
    def __init__(self, repository: AcademicPeriodRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
