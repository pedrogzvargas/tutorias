from tutorias_itsvc.students.repositories import StudentInstituteRepository


class InstituteFilterService:
    def __init__(self, repository: StudentInstituteRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
