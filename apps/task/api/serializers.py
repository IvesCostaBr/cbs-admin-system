from rest_framework import serializers
from ..models import TaskApi
from apps.collaborator.api.serializers import CollaboratorSerializer


class TaskSerializer(serializers.ModelSerializer):
    # owner = CollaboratorSerializer(many=True)
    class Meta:
        model = TaskApi
        fields = ['id', 'title', 'description', 'owner']
