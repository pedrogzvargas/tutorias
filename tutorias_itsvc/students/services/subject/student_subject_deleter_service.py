from tutorias_itsvc.students.repositories import StudentSubjectRepository


class StudentSubjectDeleterService:
    def __init__(self, repository: StudentSubjectRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
