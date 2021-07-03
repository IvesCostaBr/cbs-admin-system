from django.urls import path
from .views import (
    PainelTask,
    CreateTask,
    ListTasks,
    UpdateTask,
    relatorio_pdf,
    taskComplete,
    DetailTask,
    filtertask,
    myTasks,
)


urlpatterns = [

    path('', PainelTask.as_view(), name='painel_task'),
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path('list_tasks/', ListTasks.as_view(), name='list_tasks'),
    path('edit_tasks/<int:pk>/', UpdateTask.as_view(), name='edit_task'),
    path('relatorio/', relatorio_pdf, name='relatorio_pdf'),
    path('task-complete/<int:id>/', taskComplete, name='taskComplete'),
    path('task-detail/<int:pk>/', DetailTask.as_view(), name='detail_task'),
    path('filter-task/',filtertask , name='filter-task'),
    path('list_my_task/', myTasks, name='list_my_task'),
]
