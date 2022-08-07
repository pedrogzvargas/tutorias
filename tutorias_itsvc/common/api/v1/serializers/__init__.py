from tutorias_itsvc.common.serializers.api.v1.gender.gender_serializer import GenderSerializer
from tutorias_itsvc.common.serializers.api.v1.state.state_serializer import StateSerializer
from tutorias_itsvc.common.serializers.api.v1.academic_degree.academic_degree import AcademicDegreeSerializer
from .address_seralizer import AddressSerializer
from tutorias_itsvc.common.serializers.api.v1.personal_relationships.attitude_serializer import AttitudeSerializer
from tutorias_itsvc.common.serializers.api.v1.disability.disability_serializer import DisabilitySerializer
from tutorias_itsvc.common.serializers.api.v1.address.home_status_serializer import HomeStatusSerializer
from tutorias_itsvc.common.serializers.api.v1.address.housing_type_serializer import HousingTypeSerializer
from tutorias_itsvc.common.serializers.api.v1.income.income_serializer import IncomeSerializer
from tutorias_itsvc.common.serializers.api.v1.marital_status.marital_status_serializer import MaritalStatusSerializer
from tutorias_itsvc.common.serializers.api.v1.personal_relationships.relationshipt_serializer import RelationshipSerializer
from tutorias_itsvc.common.serializers.api.v1.school_cycle.school_cycle_serializer import SchoolCycleSerializer


__all__ = [
    'GenderSerializer',
    'StateSerializer',
    'AcademicDegreeSerializer',
    'AddressSerializer',
    'AttitudeSerializer',
    'DisabilitySerializer',
    'HomeStatusSerializer',
    'HousingTypeSerializer',
    'IncomeSerializer',
    'MaritalStatusSerializer',
    'RelationshipSerializer',
    'SchoolCycleSerializer',
]
