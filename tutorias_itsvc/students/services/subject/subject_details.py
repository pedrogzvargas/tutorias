from django.db.models import Sum


class SubjectDetailsService:
    def __init__(self,
                 student_repository=None,
                 academic_subject_repository=None,
                 student_subject_repository=None,
                 academic_information_repository=None):

        self.__student_repository = student_repository
        self.__academic_subject_repository = academic_subject_repository
        self.__student_subject_repository = student_subject_repository
        self.__academic_information_repository = academic_information_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        subject_details = None
        if not student:
            raise Exception("No existe el usuario")
        select_related = [
            'academic_information__academic_period_number__academic_period__academic_major__university',
            'academic_information__academic_period_number__academic_period__academic_major__major',
            'academic_information__academic_period_number__academic_period__period',
            'academic_information__group',
            'academic_information__academic_period_number__period_number',
            'student'
        ]
        academic_information = self.__academic_information_repository.get(select_related=select_related,
                                                                          student_id=student.id)
        if academic_information:
            major_id = academic_information.academic_information.academic_period_number.academic_period.academic_major.major.id
            major_subjects = self.__academic_subject_repository.filter(
                academic_period_number__academic_period__academic_major__major_id=major_id,
            )
            taking_subjects = self.__student_subject_repository.filter(student_id=student_id,
                                                                       approved__isnull=True,
                                                                       unsubscribed=False)

            approved_subjects = self.__student_subject_repository.filter(student_id=student_id, approved=True)
            failed_subjects = self.__student_subject_repository.filter(student_id=student_id, approved=False)

            approved_subjects_sum = approved_subjects.aggregate(
                Sum('tutor_subject__subject__total_value')).get('tutor_subject__subject__total_value__sum') or 0

            taking_subjects_sum = taking_subjects.aggregate(
                Sum('tutor_subject__subject__total_value')).get('tutor_subject__subject__total_value__sum') or 0

            subject_details = dict(
                subjects=major_subjects.count(),
                taking_subjects=taking_subjects.count(),
                approved_subjects=approved_subjects.count(),
                failed_subjects=failed_subjects.count(),
                approved_subjects_points=approved_subjects_sum,
                taking_subjects_points=taking_subjects_sum,
                total_points=approved_subjects_sum + taking_subjects_sum
            )
        return subject_details
