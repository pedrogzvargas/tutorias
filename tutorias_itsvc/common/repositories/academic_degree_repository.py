from shared.repositories import Repository
from tutorias_itsvc.common.models import AcademicDegree


class AcademicDegreeRepository(Repository):
    def __init__(self, model=None):
        model = model or AcademicDegree
        super(AcademicDegreeRepository, self).__init__(model)
