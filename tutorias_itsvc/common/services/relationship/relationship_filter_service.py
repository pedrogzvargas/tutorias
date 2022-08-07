from tutorias_itsvc.common.repositories import RelationshipRepository


class RelationshipFilterService:
    def __init__(self, repository: RelationshipRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
