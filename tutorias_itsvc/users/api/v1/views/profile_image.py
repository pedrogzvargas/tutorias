import logging
import uuid
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tutorias_itsvc.users.api.v1.serializers import ProfileImage as ProfileImageSerializer
from tutorias_itsvc.users.services import ProfileImage as ProfileImageService, ProfileImageManager, User as UserService
from tutorias_itsvc.utils import Base64Image


class ProfileImage(APIView):
    permission_classes = ()
    def get(self, request, user_id: int):
        try:
            user = UserService.get_by_id(user_id)
            profile_image = ProfileImageService(user=user).get()
            serializer = ProfileImageSerializer(profile_image, context={"request": request})
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"ProfileImage::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )

    def put(self, request, user_id: int):
        try:
            user = UserService.get_by_id(user_id)
            serializer = ProfileImageSerializer(data=request.data)
            if not serializer.is_valid():
                raise Exception(serializer.errors)
            base64data = serializer.data.get('profile_image')
            name = f"{user.username}-{uuid.uuid4()}"
            profile_image = Base64Image.create(base64data=base64data, name=name)
            profile_image_info = dict(profile_image=profile_image)
            profile_image = ProfileImageManager(user).create(profile_image_info)
            serializer = ProfileImageSerializer(profile_image)
            return Response(serializer.data, status.HTTP_200_OK)
        except Exception as err:
            logging.info(f"ProfileImage::put Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
