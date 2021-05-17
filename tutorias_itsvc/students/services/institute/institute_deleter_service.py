from tutorias_itsvc.students.repositories import StudentInstituteRepository


class InstituteDeleterService:
    def __init__(self, repository: StudentInstituteRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
