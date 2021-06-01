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
    path('home_collaborator/<int:pk>/', CollaboratorPage.as_view(), name='collaborator_page'),
    path('create_collaborator/', CreateCollaborator.as_view(), name='new_collaborator'),
    path('painel_collaborator/', HomeCollaboratorPainelAdmin.as_view(), name='painel_collaborator'),
    path('edit_collaborator/<int:pk>/', EditDataCollaborator.as_view(), name='edit_collaborator'),
    path('list_collaborator/', ListCollaborators.as_view(), name='list_collaborators'),
    path('collaborator_delete/<int:pk>/',CollaboratorDelete.as_view(), name='collaborator_delete'),
    path('collaborator_detail/<int:pk>/', CollaboratorDetail.as_view(), name='collaborator_detail'),
]
 