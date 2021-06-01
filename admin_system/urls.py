from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from rest_framework import routers
from apps.core.views import UserViewSet, GroupViewSet
from apps.collaborator.api.views_api import CollaboratorViewSet
from apps.register_extra_hour.api.views_api import ExtraHourViewSet
from apps.company.api.views_api import CompanyViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'collaborator', CollaboratorViewSet)
router.register(r'extra_hour', ExtraHourViewSet)
router.register(r'company', CompanyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('login/', views.LoginView.as_view(
        template_name='registration/login.html',
    ), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
