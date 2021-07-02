from django.contrib.auth.models import User
from .models import Collaborator

#FUNCTIONS REDUCE


def createCollaborator(form, request):
    user = User.objects.create(
        first_name=form.cleaned_data['first_name'],
        last_name=form.cleaned_data['last_name'],
        username=form.cleaned_data['email'],
        email=form.cleaned_data['email'],
        password=form.cleaned_data['email'],
    )
    collaborator = Collaborator.objects.create(
        user=user,
        cpf=form.cleaned_data['cpf'],
        company=request.user.collaborator.company,
    )
    collaborator.save()
    user.save()
