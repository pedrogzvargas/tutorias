from tutorias_itsvc.students.repositories import AcademicInformationRepository


class AcademicInformationGetterService:
    def __init__(self, repository: AcademicInformationRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        select_related = [
            'academic_information__academic_period_number__academic_period__academic_major__university',
            'academic_information__academic_period_number__academic_period__academic_major__major',
            'academic_information__academic_period_number__academic_period__period',
            'academic_information__group',
            'academic_information__academic_period_number__period_number',
            'student'
        ]
        return self.__repository.get(select_related=select_related, **kwargs)
