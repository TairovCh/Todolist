from django.urls import path
from webapp.views import TaskView, CreateTask, UpdateTask, DeleteTask, IndexView, ProjectIndexView, CreateProject, ProjectView, ProjectDelete, ProjectUpdate
from django.views.generic import RedirectView


app_name = 'webapp'

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='webapp:index')),
    path('task/', IndexView.as_view(), name='index'),
    path('task/create/', CreateTask.as_view(), name='create_task'),
    path('task/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('task/<int:pk>/update/', UpdateTask.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', DeleteTask.as_view(), name='task_delete'),
    path('project/', ProjectIndexView.as_view(), name='project_index'),
    path('project/create/', CreateProject.as_view(), name='create_project'),
    path('project/view/<int:pk>/', ProjectView.as_view(), name='project_view'),
    path('project/<int:pk>/update/', ProjectUpdate.as_view(), name='project_update'),
    path('rpoject/<int:pk>/delete/', ProjectDelete.as_view(), name='project_delete'),
]