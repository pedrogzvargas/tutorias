import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tutorias_itsvc.users.api.v1.serializers import User as UserSerializer
from tutorias_itsvc.users.services import User as UserService, UserManager


class User(APIView):
    permission_classes = ()
    def get(self, request, user_id: int):
        try:
            user = UserService.get_by_id(user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"Student::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, user_id: int):
        try:
            user = UserService.get_by_id(user_id)
            serializer = UserSerializer(data=request.data, context={'user': user})
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            UserManager(user).update(serializer.data)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"Student::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
