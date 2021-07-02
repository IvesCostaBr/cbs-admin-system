#encode utf-8
from django.http.response import HttpResponse
from apps.core.forms import RegisterUser
from django.shortcuts import  redirect, render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Notification
from apps.collaborator.models import Collaborator

from .others.functions_extra import compressed

#--------------------API-----------------------------#

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from .serializers import UserSerializer, GroupSerializer

#----------------------API-----------------------------#

from django.views.generic.base import View
from django.urls import reverse


#TODO:setar permições nas views
#TODO:Assim que o USER entra ele não é um colcaborator verificar se ele é ou não antes de deixar ele cadastrar uma empresa
class HomePage(LoginRequiredMixin, TemplateView):
    template_name = 'core/home_page_admin.html'

    def get_context_data(self,  *args, **kwargs):
        context = super().get_context_data( *args, **kwargs)
        context['notifications'] = Notification.objects.all().order_by('-id')[:4]
        return context


    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.has_perm('core.gerente_geral'):
            return HttpResponse('<h3>Sem permissão amigo:(!</h3>')
        return super(HomePage, self).dispatch(request, *args, **kwargs)
    
class Redirect(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            if self.request.user.company_set.first():
                return redirect('home_page_admin')
            else:
                return redirect('create_company')
        else:
            if not Collaborator.objects.filter(user=self.request.user).exists():
                return HttpResponse("Você não está registrado em nenhuma empresa<a href="">Voltar</a>")
            return redirect(reverse('collaborator_page', args=[self.request.user.collaborator.id]))



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

class CreateUser(View):
    def get(self, request, *args, **kwargs):
        form = RegisterUser
        return render(self.request, 'registration/sig-in.html', {'form':form})

    def post(self, request, *args, **kwargs):
        form = RegisterUser(request.POST or None)
        if form.is_valid():
            if form.cleaned_data['password1'] == form.cleaned_data['password2']:
                compressed(form)
                return redirect('login')
        return render(self.request, 'registration/sig-in.html', {'form': form})
