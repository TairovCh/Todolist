
"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import TaskView, CreateTask, UpdateTask, DeleteTask, IndexView, ProjectIndexView, CreateProject, ProjectView, ProjectDelete, ProjectUpdate
from accounts.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('create/', CreateTask.as_view(), name='create_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/<int:pk>/update/', UpdateTask.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', DeleteTask.as_view(), name='task_delete'),
    path('project/', ProjectIndexView.as_view(), name='project_index'),
    path('project/create/', CreateProject.as_view(), name='create_project'),
    path('project/view/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project_update'),
    path('rpoject/<int:pk>/delete/', ProjectDelete.as_view(), name='project_delete'),
    path('accounts/login', login_view, name='login'),
    path('accounts/logout/', logout_view, name='logout'),
]
