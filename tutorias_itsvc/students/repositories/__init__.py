from .student_repository import StudentRepository
from .academic_information_repository import AcademicInformationRepository
from .student_institute_repository import StudentInstituteRepository
from .phone_repository import StudentPhoneRepository
from .medical_information_repository import MedicalInformationRepository
from .address import AddressRepository
from .parent_repository import ParentRepository
from .student_income_repository import StudentIncomeRepository
from .student_sibling_repository import StudentSiblingRepository
from .student_subject_repository import StudentSubjectRepository


__all__ = [
    'StudentRepository',
    'AcademicInformationRepository',
    'StudentInstituteRepository',
    'StudentPhoneRepository',
    'MedicalInformationRepository',
    'AddressRepository',
    'ParentRepository',
    'StudentIncomeRepository',
    'StudentSiblingRepository',
    'StudentSubjectRepository',
]
