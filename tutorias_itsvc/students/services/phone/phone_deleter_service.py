from tutorias_itsvc.students.repositories import StudentPhoneRepository


class PhoneDeleterService:
    def __init__(self, repository: StudentPhoneRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
