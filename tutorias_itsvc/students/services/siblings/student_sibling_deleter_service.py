from tutorias_itsvc.students.repositories import StudentSiblingRepository


class StudentSiblingDeleterService:
    def __init__(self, repository: StudentSiblingRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
