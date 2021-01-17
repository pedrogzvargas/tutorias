from .api_exception import ApiException


class SerializerApiException(ApiException):
    def __init__(self, message, http_status=400, errors={}):
        super(SerializerApiException, self).__init__(message, http_status)
        self.errors = errors
