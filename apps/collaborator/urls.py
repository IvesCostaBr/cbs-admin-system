from django.urls import path
from .views import (
    CreateCollaborator,
    EditDataCollaborator,
    ListCollaborators,
    CollaboratorDelete,
    CollaboratorDetail,
    HomeCollaboratorPainelAdmin,
    CollaboratorPage,
)

urlpatterns = [
    path('home_collaborator/', HomeCollaboratorPainelAdmin.as_view(), name='home_collaborator'),
    path('create_collaborator/', CreateCollaborator.as_view(), name='new_collaborator'),
    path('collaborator_page/<int:pk>/', CollaboratorPage.as_view(), name='collaobrator_page'),
    path('edit_collaborator/<int:pk>/', EditDataCollaborator.as_view(), name='edit_collaborator'),
    path('list_collaborator/', ListCollaborators.as_view(), name='list_collaborators'),
    path('collaborator_delete/<int:pk>/',CollaboratorDelete.as_view(), name='collaborator_delete'),
    path('collaborator_detail/<int:pk>/', CollaboratorDetail.as_view(), name='collaborator_detail'),
]
