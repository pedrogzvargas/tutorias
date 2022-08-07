from shared.repositories import Repository
from tutorias_itsvc.students.models import OrganizacionEstudio


class OrganizacionEstudioRepository(Repository):
    def __init__(self, model=None):
        model = model or OrganizacionEstudio
        super(OrganizacionEstudioRepository, self).__init__(model)
