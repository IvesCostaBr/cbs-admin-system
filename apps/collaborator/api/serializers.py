from rest_framework import serializers
from ..models import Collaborator
from apps.register_extra_hour.api.serializers import ExtraHourSerializer


class CollaboratorSerializer(serializers.ModelSerializer):
    registerextrahour_set = ExtraHourSerializer(many=True)
    class Meta:
        model = Collaborator
        fields = ['user', 'departaments', 'company', 'first_name', 'last_name', 'total_horas','registerextrahour_set']
