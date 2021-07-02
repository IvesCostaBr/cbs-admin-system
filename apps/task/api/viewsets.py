from rest_framework import viewsets
from .serializers import TaskSerializer
from ..models import TaskApi


class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskApi.objects.all()
    serializer_class = TaskSerializer



    