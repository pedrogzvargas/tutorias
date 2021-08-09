from tutorias_itsvc.academy.models import Subject
from shared.repositories import Repository


class SubjectRepository(Repository):
    def __init__(self, model=None):
        model = model or Subject
        super(SubjectRepository, self).__init__(model)
