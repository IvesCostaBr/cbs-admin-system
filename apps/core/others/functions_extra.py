from apps.collaborator.models import Collaborator
from apps.company.models import Company
from django.contrib.auth.models import User
from apps.collaborator.tasks import sendEmailRegister


def compressed(form):
    form = form.cleaned_data
    newUser = User.objects.create_user(
        form['email'], 
        form['email'] ,
        form['password1'])
    newUser.first_name = form['first_name']
    newUser.last_name = form['last_name']
    newUser.save()
    collaborator = Collaborator.objects.create(user=newUser,
        company=Company.objects.get(code_company=form['company_code']))
    collaborator.save()
    sendEmailRegister(collaborator)