from rest_framework.response import Response


class ResponseService:
    def __init__(self, response=None):
        self.__response = response or Response

    def __call__(self, payload, http_status=400):
        return self.__response(payload, status=http_status)
