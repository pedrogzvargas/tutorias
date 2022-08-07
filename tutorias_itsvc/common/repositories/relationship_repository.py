from shared.repositories import Repository
from tutorias_itsvc.common.models import Relationship


class RelationshipRepository(Repository):
    def __init__(self, model=None):
        model = model or Relationship
        super(RelationshipRepository, self).__init__(model)
