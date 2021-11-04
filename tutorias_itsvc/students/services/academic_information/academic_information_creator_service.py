from tutorias_itsvc.students.services.academic_information.exceptions import AcademicInformationNotExist


class AcademicInformationCreatorService:
    def __init__(self,
                 academic_information_repository=None,
                 academic_group_repository=None):
        self.__academic_information_repository = academic_information_repository
        self.__academic_group_repository = academic_group_repository

    def __call__(self, student_id, university_id, major_id, period_id, group_id, period_number_id):
        academic_information = self.__academic_group_repository.get(
            academic_period_number__academic_period__academic_major__university_id=university_id,
            academic_period_number__academic_period__academic_major__major_id=major_id,
            academic_period_number__academic_period__period_id=period_id,
            academic_period_number__period_number_id=period_number_id,
            group_id=group_id
        )
        if not academic_information:
            raise AcademicInformationNotExist("No existe información academica")
        return self.__academic_information_repository.create(student_id=student_id,
                                                             academic_information_id=academic_information.id)
