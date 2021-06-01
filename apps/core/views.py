from django.shortcuts import HttpResponse, render, HttpResponseRedirect, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

#--------------------API-----------------------------#

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, GroupSerializer

#----------------------API-----------------------------#
from django.views.generic.base import View
from django.urls import reverse
from django.contrib.auth.decorators import login_required


#TODO:Assim que o USER entra ele não é um colcaborator verificar se ele é ou não antes de deixar ele cadastrar uma empresa
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'core/home_page_admin.html'

class Redirect(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return redirect('home_page_admin')

        return redirect(reverse('collaborator_page', args=[self.request.user.collaborator.id]))




class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)



class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
