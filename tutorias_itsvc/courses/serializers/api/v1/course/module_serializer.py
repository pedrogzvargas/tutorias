from rest_framework import serializers
from tutorias_itsvc.courses.models import Module


class ModuleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Module
        exclude = ("created_at", "updated_at", )
