from tutorias_itsvc.academy.models import AcademicMajor
from shared.repositories import Repository


class AcademicMajorRepository(Repository):
    def __init__(self, model=None):
        model = model or AcademicMajor
        super(AcademicMajorRepository, self).__init__(model)
