from shared.repositories import Repository
from tutorias_itsvc.students.models import AreaPsicopedagogica


class AreaPsicopedagogicaRepository(Repository):
    def __init__(self, model=None):
        model = model or AreaPsicopedagogica
        super(AreaPsicopedagogicaRepository, self).__init__(model)
