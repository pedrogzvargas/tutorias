from tutorias_itsvc.students.services.personal_information.exceptions import PersonalInformationNotExist
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist


class PersonalInformationDeleterService:
    def __init__(self, student_repository=None, personal_information_repository=None):
        self.__student_repository = student_repository
        self.__personal_information_repository = personal_information_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise StudentNotExist(f"No existe un usuario con el id {student_id}")

        personal_information = self.__personal_information_repository.get(user_id=student.user_id)
        if not personal_information:
            raise PersonalInformationNotExist(f"No se encontró información persona con el id de usuario {student_id}")

        return self.__personal_information_repository.delete(id=personal_information.id)
