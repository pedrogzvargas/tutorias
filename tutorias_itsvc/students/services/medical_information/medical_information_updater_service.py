from tutorias_itsvc.students.repositories import MedicalInformationRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import DisabilityRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.common.services.disability.exceptions import DisabilityNotExist
from tutorias_itsvc.students.services.medical_information.exceptions import MedicalInformationNotExist


class MedicalInformationUpdaterService:
    def __init__(self,
                 medical_information_repository: MedicalInformationRepository,
                 student_repository: StudentRepository,
                 disability_repository: DisabilityRepository):
        self.__medical_information_repository = medical_information_repository
        self.__student_repository = student_repository
        self.__disability_repository = disability_repository

    def __call__(self, medical_information_id, student_id, disability_id, description=None):
        if not self.__medical_information_repository.get(id=medical_information_id, student_id=student_id):
            raise MedicalInformationNotExist(f"No existe información medica con el id {medical_information_id}")
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise StudentNotExist(f"No existe un usuario con id {student_id}")
        disability = self.__disability_repository.get(id=disability_id)
        if not disability:
            raise DisabilityNotExist(f"No existe una discapacidad con el id {disability_id}")
        return self.__medical_information_repository.update(id=medical_information_id,
                                                            student_id=student_id,
                                                            disability_id=disability_id,
                                                            description=description)
