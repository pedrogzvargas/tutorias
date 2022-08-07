from tutorias_itsvc.tutor.models import TutorGroup
from shared.repositories import Repository


class TutorGroupRepository(Repository):
    def __init__(self, model=None):
        model = model or TutorGroup
        super(TutorGroupRepository, self).__init__(model)
