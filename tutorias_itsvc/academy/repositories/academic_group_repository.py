from tutorias_itsvc.academy.models import AcademicGroup
from shared.repositories import Repository


class AcademicGroupRepository(Repository):
    def __init__(self, model=None):
        model = model or AcademicGroup
        super(AcademicGroupRepository, self).__init__(model)
