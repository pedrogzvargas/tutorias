from django.contrib.auth import authenticate
from tutorias_itsvc.users.services.token import TokenGetterService, TokenCreatorService
from tutorias_itsvc.users.repositories import TokenRepository


class DjangoLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __call__(self):
        user = authenticate(username=self.username, password=self.password)
        if not user:
            raise ValueError('Invalid credentials')
        repository = TokenRepository()
        toke_service = TokenGetterService(repository)
        token = toke_service(user=user)
        if not token:
            token_creator_service = TokenCreatorService(repository)
            token = token_creator_service(user=user)
        return token
