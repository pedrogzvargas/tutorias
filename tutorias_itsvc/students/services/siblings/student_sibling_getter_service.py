from tutorias_itsvc.students.repositories import StudentSiblingRepository


class StudentSiblingGetterService:
    def __init__(self, repository: StudentSiblingRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
