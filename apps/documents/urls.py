from django.urls import path
from .views import (
    CreateDocument,
    HomeDocument,
    UpdateDocument,
    DeleteDocument,
    DetailDocument,
    ListDocument,
)

urlpatterns = [
    path('', HomeDocument.as_view() , name='home_documents'),
    path('create_document/', CreateDocument.as_view(), name='create_document'),
    path('list_documents/', ListDocument.as_view(), name='list_documents'),
    path('update_document/<int:pk>/', UpdateDocument.as_view(), name='update_document'),
    path('delete_document/<int:pk>/', DeleteDocument.as_view(), name='delete_document'),
    path('detail_document/<int:pk>/', DetailDocument.as_view(), name='detail_document')
    
]