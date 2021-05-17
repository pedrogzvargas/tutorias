import uuid
from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.utils import Base64Image
from shared.exceptions import SerializerApiException
from tutorias_itsvc.users.services.profile_image import ProfileImageCreatorService
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.services.user import UserGetterService

log = get_logger(__file__)


class ProfileImageCreatorController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or ProfileImageCreatorService(self.__repository)

    def get_user(self, user_id):
        repository = UserRepository()
        getter_service = UserGetterService(repository)
        user = getter_service(id=user_id)
        return user

    def __call__(self, user_id):
        try:
            user = self.get_user(user_id=user_id)
            if not user:
                raise Exception(f"No existe un usuario con el id {user_id}")
            fields = self.__request.get_data()
            base64data = fields.get('profile_image')
            name = f"{user.username}-{uuid.uuid4()}"
            profile_image = Base64Image.create(base64data=base64data, name=name)
            fields.update(dict(user_id=user.id, profile_image=profile_image))
            self.__service(**fields)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            return self.__response(response_data, http_status=status.HTTP_201_CREATED)
        except SerializerApiException as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                errors=err.errors
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in ProfileImageCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
