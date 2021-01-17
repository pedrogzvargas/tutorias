from rest_framework.authtoken.models import Token
from shared.repositories import Repository


class TokenRepository(Repository):

    def __init__(self, model=Token):
        super(TokenRepository, self).__init__(model)
