from django.contrib import admin

from task1.models import CustomUser, Task

admin.site.register(CustomUser)
admin.site.register(Task)