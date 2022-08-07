from tutorias_itsvc.students.repositories import OrganizacionEstudioRepository


class OrganizacionEstudioGetterService:
    def __init__(self, repository: OrganizacionEstudioRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
