from django.test import TestCase
from apps.collaborator.models import Collaborator
from apps.company.models import Company
from django.contrib.auth.models import User
from apps.register_extra_hour.models import RegisterExtraHour
from apps.task.models import Task


class CollaboratorTestCase(TestCase):
    def setUp(self) -> TestCase:
        user = User.objects.create_user(username='teste', password='teste')
        user.save()
        company = Company.objects.create(name="company_test")
        Collaborator.objects.create(
            user=user,
            company=company,
        )
        
    
    def testNewCollaborator(self) -> TestCase:
        collaborator =  Collaborator.objects.last()
        RegisterExtraHour.objects.create(
            reason="teste unit",
            collaborator=collaborator,
            status=True,
            hours=15.5
        )
        
    
    def testCalculateHour(self):
        collaborator = Collaborator.objects.last()
        collaborator.somar_horas()
        self.assertEqual(collaborator.total_horas,  0.00)
    
    def testNewTask(self):
        assert 1+1 == 2
        
    
    