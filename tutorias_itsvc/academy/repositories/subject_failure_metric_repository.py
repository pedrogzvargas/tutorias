from tutorias_itsvc.academy.models import SubjectFailureMetric
from shared.repositories import Repository


class SubjectFailureMetricRepository(Repository):
    def __init__(self, model=None):
        model = model or SubjectFailureMetric
        super(SubjectFailureMetricRepository, self).__init__(model)
