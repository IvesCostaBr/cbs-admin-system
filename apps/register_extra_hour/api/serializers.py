from rest_framework import serializers
from ..models import RegisterExtraHour


class ExtraHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterExtraHour
        fields = ['reason', 'date', 'collaborator', 'hours', 'status']
