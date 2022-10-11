import pandas as pd
from io import BytesIO
import base64
from django.db import transaction
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import StudentSubjectRepository
from tutorias_itsvc.tutor.repositories import TutorSubjectRepository
from tutorias_itsvc.academy.repositories import SubjectTypeRepository
from tutorias_itsvc.common.repositories import SchoolCycleRepository
from tutorias_itsvc.academy.repositories import SubjectFailureMetricRepository


class StudentsSubjectLoaderService:
    def __init__(
        self,
        student_repository: StudentRepository,
        student_subject_repository: StudentSubjectRepository,
        tutor_subject_repository: TutorSubjectRepository,
        subject_type_repository: SubjectTypeRepository,
        school_cycle_repository: SchoolCycleRepository,
        failed_metric_repository: SubjectFailureMetricRepository,
    ):
        self.__student_repository = student_repository
        self.__student_subject_repository = student_subject_repository
        self.__tutor_subject_repository = tutor_subject_repository
        self.__subject_type_repository = subject_type_repository
        self.__school_cycle_repository = school_cycle_repository
        self.__failed_metric_repository = failed_metric_repository

    @transaction.atomic
    def __call__(self, **kwargs):
        base64_as_string = kwargs.get('file')
        file_as_bytes = base64.b64decode(base64_as_string)
        data_frame = pd.read_csv(BytesIO(file_as_bytes), keep_default_na=False)
        dataframe_as_dict = data_frame.to_dict(orient='records')
        for subject in dataframe_as_dict:
            student_enrollment = subject.get('enrollment')
            student = self.__student_repository.get(enrollment=student_enrollment)
            if not student:
                raise Exception(f'No existe un usuario con esta matricula {student_enrollment}')

            school_cycle = self.__school_cycle_repository.get(name=subject.get("school_cycle"))
            if not school_cycle:
                raise Exception(f'No existe un ciclo escolar con el nombre {subject.get("school_cycle")}')

            subject_type = self.__subject_type_repository.get(name=subject.get("type"))
            if not subject_type:
                raise Exception(f'No existe un tipo de materis con el nombre {subject.get("type")}')

            failure_metric = self.__failed_metric_repository.get(name=subject.get("failure_metric"))
            if not failure_metric:
                raise Exception(f'No existe una metrica con el nombre {subject.get("failure_metric")}')

            tutor_subject = self.__tutor_subject_repository.get(subject__code=subject.get("subject_code"), tutor__enrollment=subject.get("tutor_enrollment"))
            if not tutor_subject:
                raise Exception(f'No existe una materia impartida con el codigo {subject.get("subject_code")}')

            self.__student_subject_repository.create(
                student_id=student.id,
                tutor_subject_id=tutor_subject.id,
                type_id=subject_type.id,
                approved=subject.get('approved') if subject.get('approved') else None,
                final_score=subject.get('final_score') if subject.get('final_score') else None,
                failure_metric_id=failure_metric.id,
                comment=subject.get('comment'),
                school_cycle_id=school_cycle.id,
                unsubscribed=subject.get('unsubscribed')
            )
