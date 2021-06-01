from django.urls import path, include
from .views import (
    HomePage,
    Redirect,

)

urlpatterns = [
    path('', Redirect.as_view(), name='redirect'),
    path('admin-system/', HomePage.as_view(), name='home_page_admin'),
    path('company/',include('apps.company.urls')),
    path('deparaments/', include('apps.departament.urls')),
    path('collaborator/',include('apps.collaborator.urls')),
    path('documents/', include('apps.documents.urls')),
    path('hourdatabase/', include('apps.register_extra_hour.urls')),
    path('task/', include('apps.task.urls')),
    
]
