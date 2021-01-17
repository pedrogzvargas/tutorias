from tutorias_itsvc.academy.models import Major
from shared.repositories import Repository


class MajorRepository(Repository):
    def __init__(self, model=None):
        model = model or Major
        super(MajorRepository, self).__init__(model)
