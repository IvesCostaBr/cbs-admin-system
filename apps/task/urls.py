from django.urls import path
from .views import (
    PainelTask,
    CreateTask,
    ListTasks,
    UpdateTask,
    relatorio_pdf
)


urlpatterns = [

    path('', PainelTask.as_view(), name='painel_task'),
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path('list_tasks/', ListTasks.as_view(), name='list_tasks'),
    path('edit_tasks/<int:pk>/', UpdateTask.as_view(), name='edit_task'),
    path('relatorio/', relatorio_pdf, name='relatorio_pdf'),
]
