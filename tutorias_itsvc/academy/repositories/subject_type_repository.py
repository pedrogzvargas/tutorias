from tutorias_itsvc.academy.models import SubjectType
from shared.repositories import Repository


class SubjectTypeRepository(Repository):
    def __init__(self, model=None):
        model = model or SubjectType
        super(SubjectTypeRepository, self).__init__(model)
