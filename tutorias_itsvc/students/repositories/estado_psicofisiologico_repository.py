from shared.repositories import Repository
from tutorias_itsvc.students.models import EstadoPsicofisiologico


class EstadoPsicofisiologicoRepository(Repository):
    def __init__(self, model=None):
        model = model or EstadoPsicofisiologico
        super(EstadoPsicofisiologicoRepository, self).__init__(model)
