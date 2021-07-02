from django.contrib import admin
from django.urls import path, include
from apps.collaborator.views import LoginEnable, LoginDisable

from rest_framework import routers
from apps.core.views import UserViewSet, GroupViewSet
from apps.collaborator.api.views_api import CollaboratorViewSet
from apps.register_extra_hour.api.views_api import ExtraHourViewSet
from apps.company.api.views_api import CompanyViewSet
from apps.task.api.viewsets import TaskViewSet

from django.contrib.auth import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'collaborator', CollaboratorViewSet)
router.register(r'extra_hour', ExtraHourViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'task-api', TaskViewSet)


urlpatterns = [
    
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('login/', LoginEnable.as_view(
        template_name='registration/login.html',
    ), name='login'),
    path('logout/', LoginDisable.as_view(), name='logout'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
] 
