from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import CollaboratorSerializer
from ..models import Collaborator

class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)