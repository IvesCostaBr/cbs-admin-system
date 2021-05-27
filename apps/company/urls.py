from django.urls import path
from .views import (
    CreateCompany,
    ListCompany,
    UpdateCompany,
    DeleteCompany,
)

urlpatterns = [
    path('create-company/', CreateCompany.as_view(), name='create_company'),
    path('list-company/', ListCompany.as_view(), name='list_company'),
    path('delete-company/<int:pk>/', DeleteCompany.as_view(), name='delete_company'),
    path('update-company<int:pk>/',UpdateCompany.as_view(), name='update_company'),
]
