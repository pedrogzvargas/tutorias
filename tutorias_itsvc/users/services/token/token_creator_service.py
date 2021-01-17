from tutorias_itsvc.users.repositories import TokenRepository


class TokenCreatorService:
    def __init__(self, repository: TokenRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
