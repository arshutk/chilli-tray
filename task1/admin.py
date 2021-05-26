from django.contrib import admin

from task1.models import CustomUser, Task


class UserAdmin(admin.ModelAdmin):
    ''' Custom User Admin, basically makes join_date and last_login field readonly in Admin Panel'''
    
    readonly_fields = ('join_date', 'last_login', 'password')
    list_display = ('username', 'is_active', 'is_superuser', 'is_staff')
    search_fields = ('username',)
    list_filter = ('is_active', 'is_superuser', 'is_staff')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_title', 'user',)
    search_fields = ('task_title',)
    list_filter = ('user',)
    readonly_fields = ('create_time_stamps',)




admin.site.register(CustomUser, UserAdmin)
admin.site.register(Task, TaskAdmin)