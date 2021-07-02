from django.contrib import admin
from apps.task.models import Task, TaskApi

admin.site.register(Task)
admin.site.register(TaskApi)