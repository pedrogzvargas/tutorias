from shared.repositories import Repository
from tutorias_itsvc.students.models import AreaIntegracion


class AreaIntegracionRepository(Repository):
    def __init__(self, model=None):
        model = model or AreaIntegracion
        super(AreaIntegracionRepository, self).__init__(model)
