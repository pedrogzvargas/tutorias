from tutorias_itsvc.users.repositories import ProfileImageRepository


class ProfileImageCreatorService:
    def __init__(self, repository: ProfileImageRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
