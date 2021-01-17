class ApiException(Exception):
    def __init__(self, message, http_status=400):
        super(ApiException, self).__init__(message)
        self.http_status = http_status
