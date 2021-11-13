from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.users.repositories import SiblingRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import StudentSiblingRepository
from tutorias_itsvc.common.repositories import GenderRepository
from tutorias_itsvc.common.repositories import AcademicDegreeRepository
from tutorias_itsvc.common.repositories import RelationshipRepository
from tutorias_itsvc.common.repositories import AttitudeRepository
from tutorias_itsvc.students.services.siblings import StudentSiblingCreatorService

log = get_logger(__file__)


class SiblingCreatorController:
    def __init__(self,
                 request,
                 response,
                 sibling_repository=None,
                 student_repository=None,
                 student_sibling_repository=None,
                 gender_repository=None,
                 academic_degree_repository=None,
                 relationship_repository=None,
                 attitude_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__sibling_repository = sibling_repository or SiblingRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__student_sibling_repository = student_sibling_repository or StudentSiblingRepository()
        self.__gender_repository = gender_repository or GenderRepository()
        self.__academic_degree_repository = academic_degree_repository or AcademicDegreeRepository()
        self.__relationship_repository = relationship_repository or RelationshipRepository()
        self.__attitude_repository = attitude_repository or AttitudeRepository()
        self.__service = service or StudentSiblingCreatorService(
            sibling_repository=self.__sibling_repository,
            student_repository=self.__student_repository,
            student_sibling_repository=self.__student_sibling_repository,
            gender_repository=self.__gender_repository,
            academic_degree_repository=self.__academic_degree_repository,
            relationship_repository=self.__relationship_repository,
            attitude_repository=self.__attitude_repository)

    def __call__(self, student_id):
        try:
            fields = self.__request.get_data()
            self.__service(student_id=student_id, **fields)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            return self.__response(response_data, http_status=status.HTTP_201_CREATED)
        except SerializerApiException as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                errors=err.errors
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in SiblingCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
