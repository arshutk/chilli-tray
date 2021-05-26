from django.urls import path

from user_task.views import (registration_view, login_view, home_view, logout_view, task_create_view)


urlpatterns = [
    path('register/', registration_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('task/create/', task_create_view, name='task_create'),
    path('home/', home_view, name='home')
]