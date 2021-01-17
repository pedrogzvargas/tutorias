import logging
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from tutorias_itsvc.common.api.v1.serializers import GenderSerializer
from tutorias_itsvc.common.models import Gender


class GenderView(APIView):
    permission_classes = ()
    def get(self, request):
        try:
            genders = Gender.objects.all()
            serializer = GenderSerializer(genders, many=True)
            return Response(serializer.data, status.HTTP_200_OK)
        except (ObjectDoesNotExist, Exception) as err:
            logging.info(f"CategoriesView::get Error: {err}")
            return Response(
                dict(success=False, message=f"{err}"),
                status.HTTP_400_BAD_REQUEST
            )
