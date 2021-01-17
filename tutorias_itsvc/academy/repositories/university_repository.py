from tutorias_itsvc.academy.models import University
from shared.repositories import Repository


class UniversityRepository(Repository):
    def __init__(self, model=None):
        model = model or University
        super(UniversityRepository, self).__init__(model)
