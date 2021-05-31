from django.urls import path
from .views import (
    HomeHourDatabase,
    CreateHourExtra,
    ListHourExtra,
    UpdateHourExtra,
    DeleteHourExtra,
    DetailHourExtra,
    UtilizarHoraExtra,
)

urlpatterns = [
    path('', HomeHourDatabase.as_view(), name='painel_hour'),
    path('list_hour/',ListHourExtra.as_view(), name='list_hour'),
    path('create_hour_extra/',CreateHourExtra.as_view(),name='create_hour_extra'),
    path('update_hour_extra/<int:pk>/', UpdateHourExtra.as_view(), name='update_hour_extra'),
    path('delete_hour_extra/<int:pk>/', DeleteHourExtra.as_view(), name='delete_hour_extra'),
    path('detail_hour_extra/<int:pk>/', DetailHourExtra.as_view(), name='detail_hour_'),
    path('utilizar_hora/<int:pk>/', UtilizarHoraExtra.as_view(), name='utilizar_utilizar_hora')
]
