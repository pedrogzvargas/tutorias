from tutorias_itsvc.academy.models import AcademicSubject
from shared.repositories import Repository


class AcademicSubjectRepository(Repository):
    def __init__(self, model=None):
        model = model or AcademicSubject
        super(AcademicSubjectRepository, self).__init__(model)
