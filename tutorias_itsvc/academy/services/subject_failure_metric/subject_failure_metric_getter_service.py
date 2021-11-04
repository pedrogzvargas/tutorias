from tutorias_itsvc.academy.repositories import SubjectFailureMetricRepository


class SubjectFailureMetricGetterService:
    def __init__(self, repository: SubjectFailureMetricRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
