from tutorias_itsvc.academy.models import AcademicPeriod
from shared.repositories import Repository


class AcademicPeriodRepository(Repository):
    def __init__(self, model=None):
        model = model or AcademicPeriod
        super(AcademicPeriodRepository, self).__init__(model)
