from tutorias_itsvc.students.repositories import MedicalInformationRepository
from tutorias_itsvc.students.services.medical_information.exceptions import MedicalInformationNotExist


class MedicalInformationDeleterService:
    def __init__(self, medical_information_repository: MedicalInformationRepository):
        self.__medical_information_repository = medical_information_repository

    def __call__(self, medical_information_id, student_id):
        if not self.__medical_information_repository.get(id=medical_information_id, student_id=student_id):
            raise MedicalInformationNotExist(f"No existe información medica con el id {medical_information_id}")
        return self.__medical_information_repository.delete(id=medical_information_id)
