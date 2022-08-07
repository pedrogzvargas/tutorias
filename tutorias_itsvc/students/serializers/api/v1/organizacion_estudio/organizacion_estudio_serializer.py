from tutorias_itsvc.students.models import OrganizacionEstudio
from rest_framework import serializers


class OrganizacionEstudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizacionEstudio
        fields = '__all__'

        read_only_fields = [
            'student',
        ]
