from django.db import transaction
from tutorias_itsvc.students.repositories import StudentSiblingRepository
from tutorias_itsvc.users.repositories import SiblingRepository
from tutorias_itsvc.common.repositories import GenderRepository
from tutorias_itsvc.common.repositories import AcademicDegreeRepository
from tutorias_itsvc.common.repositories import RelationshipRepository
from tutorias_itsvc.common.repositories import AttitudeRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.services.gender.exceptions import GenderNotExist
from tutorias_itsvc.common.services.academic_degree.exceptions import AcademicDegreeNotExist
from tutorias_itsvc.common.services.relationship.exceptions import RelationshipNotExist
from tutorias_itsvc.common.services.attitude.exceptions import AttitudeNotExist
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist


class StudentSiblingCreatorService:
    def __init__(self,
                 sibling_repository: SiblingRepository,
                 student_repository: StudentRepository,
                 student_sibling_repository: StudentSiblingRepository,
                 gender_repository: GenderRepository,
                 academic_degree_repository: AcademicDegreeRepository,
                 relationship_repository: RelationshipRepository,
                 attitude_repository: AttitudeRepository):
        self.__sibling_repository = sibling_repository
        self.__student_repository = student_repository
        self.__student_sibling_repository = student_sibling_repository
        self.__gender_repository = gender_repository
        self.__academic_degree_repository = academic_degree_repository
        self.__relationship_repository = relationship_repository
        self.__attitude_repository = attitude_repository

    @transaction.atomic
    def __call__(self,
                 student_id,
                 first_name,
                 last_name,
                 gender_id,
                 birth_date,
                 academic_degree_id,
                 relationship_id,
                 attitude_id,
                 second_name=None,
                 second_last_name=None,
                 ):

        if not self.__student_repository.get(id=student_id):
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")

        if not self.__gender_repository.get(id=gender_id):
            raise GenderNotExist(f"No existe un genero con el id {gender_id}")

        if not self.__academic_degree_repository.get(id=academic_degree_id):
            raise AcademicDegreeNotExist(f"No existe un nivel académico con el id {academic_degree_id}")

        if not self.__relationship_repository.get(id=relationship_id):
            raise RelationshipNotExist(f"No existe un relación con el id {relationship_id}")

        if not self.__attitude_repository.get(id=attitude_id):
            raise AttitudeNotExist(f"No existe una actitud con el id {attitude_id}")

        sibling = self.__sibling_repository.create(
            first_name=first_name,
            second_name=second_name,
            last_name=last_name,
            second_last_name=second_last_name,
            gender_id=gender_id,
            birth_date=birth_date,
            academic_degree_id=academic_degree_id,
            relationship_id=relationship_id,
            attitude_id=attitude_id,
        )
        return self.__student_sibling_repository.create(student_id=student_id, sibling_id=sibling.id)
