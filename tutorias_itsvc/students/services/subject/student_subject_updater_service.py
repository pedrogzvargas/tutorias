from tutorias_itsvc.students.repositories import StudentSubjectRepository


class StudentSubjectUpdaterService:
    def __init__(self, repository: StudentSubjectRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
