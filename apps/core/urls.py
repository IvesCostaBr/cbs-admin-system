from django.urls import path, include
from .views import (
    HomePage,
)

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('company/',include('apps.company.urls')),
    path('deparaments/', include('apps.departament.urls')),
    path('collaborator/',include('apps.collaborator.urls')),
    path('documents/', include('apps.documents.urls')),
    path('hourdatabase/', include('apps.register_extra_hour.urls')),
    
]
