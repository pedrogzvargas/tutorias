from .university_repository import UniversityRepository
from .major_repository import MajorRepository
from .academic_period_repository import AcademicPeriodRepository
from .period_repository import PeriodRepository
from .period_number_repository import PeriodNumberRepository
from .group_repository import GroupRepository
from .academic_major_repository import AcademicMajorRepository
from .academic_group_repository import AcademicGroupRepository
from .academic_subject_repository import AcademicSubjectRepository
from .subject_repository import SubjectRepository
from .subject_type_repository import SubjectTypeRepository
from .subject_failure_metric_repository import SubjectFailureMetricRepository


__all__ = [
    'UniversityRepository',
    'MajorRepository',
    'AcademicPeriodRepository',
    'PeriodRepository',
    'PeriodNumberRepository',
    'GroupRepository',
    'AcademicMajorRepository',
    'AcademicGroupRepository',
    'AcademicSubjectRepository',
    'SubjectRepository',
    'SubjectTypeRepository',
    'SubjectFailureMetricRepository',
]
