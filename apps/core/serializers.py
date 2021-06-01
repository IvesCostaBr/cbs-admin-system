from django.contrib.auth.models import User, Group
from rest_framework import serializers
from apps.company.api.serializers import CompanySerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    company_set = CompanySerializer(many=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'company_set']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']