from tutorias_itsvc.students.repositories import StudentInstituteRepository


class InstituteUpdaterService:
    def __init__(self, repository: StudentInstituteRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
