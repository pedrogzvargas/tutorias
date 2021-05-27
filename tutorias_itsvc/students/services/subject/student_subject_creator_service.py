from tutorias_itsvc.students.repositories import StudentSubjectRepository


class StudentSubjectCreatorService:
    def __init__(self, repository: StudentSubjectRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
