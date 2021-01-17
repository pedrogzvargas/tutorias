import base64
import six
from django.core.files.base import ContentFile


class Base64Image:
    @staticmethod
    def create(base64data, name):
        if not isinstance(base64data, six.string_types):
            raise Exception("No base64 data")
        format, imgstr = base64data.split(';base64,')  # format ~= data:image/X,
        ext = format.split('/')[-1]  # guess file extension
        data = ContentFile(base64.b64decode(imgstr), name=name + f".{ext}")
        return data
