from django.urls import path, include
from .views import (
    HomePage
)

urlpatterns = [
    path('', HomePage.as_view(), name='home_page'),
    path('company/',include('apps.company.urls'))
]
