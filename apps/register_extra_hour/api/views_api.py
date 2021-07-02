from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import ExtraHourSerializer
from ..models import RegisterExtraHour

class ExtraHourViewSet(viewsets.ModelViewSet):
    queryset = RegisterExtraHour.objects.all()
    serializer_class = ExtraHourSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
