from tutorias_itsvc.academy.repositories import SubjectFailureMetricRepository


class SubjectFailureMetricFilterService:
    def __init__(self, repository: SubjectFailureMetricRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
