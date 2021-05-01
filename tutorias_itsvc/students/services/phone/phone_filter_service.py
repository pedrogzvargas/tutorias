from tutorias_itsvc.students.repositories import StudentPhoneRepository


class PhoneFilterService:
    def __init__(self, repository: StudentPhoneRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
