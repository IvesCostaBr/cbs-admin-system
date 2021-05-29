from django.urls import path
from .views import (
    HomeDepartament,
    ListDepartament,
    CreateDepartament,
    EditDepartament,
    DeleteDepartament,
    DetailDepartament
)


urlpatterns = [
    path('', HomeDepartament.as_view(), name='home_departament'),
    path('list_departament', ListDepartament.as_view(), name='list_departaments'),
    path('create_departament', CreateDepartament.as_view(), name='create_departament'),
    path('edit_departament/<int:pk>/', EditDepartament.as_view(), name='edit_departament'),
    path('delete_departament/<int:pk>/', DeleteDepartament.as_view(), name='delete_departament'),
    path('detail_departament/<int:pk>/', DetailDepartament.as_view(), name='detail_departament')
]
