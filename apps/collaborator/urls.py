from django.urls import path
from .views import (
    CreateCollaborator,
    home,
)

urlpatterns = [
    path('', home, name='collaborator_home'),
    path('create_collaborator/', CreateCollaborator.as_view(), name='new_collaborator'),
]
