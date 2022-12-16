from django.shortcuts import reverse
from django.core.paginator import Paginator
from webapp.models import ProjectTask
from webapp.forms import ProjectTaskForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ProjectIndexView(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'projects'
    model = ProjectTask
    ordering = '-start_date' 


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = ProjectTask


    def get_context_data(self, **kwargs):

        tasks = self.object.tasks.all()
        paginator = Paginator(tasks, 3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = super().get_context_data(**kwargs)
        context['page_obj'] = page_obj
        context['is_paginated'] = page_obj.has_other_pages()
        context['tasks'] = page_obj.object_list
        return context


class CreateProject(CreateView):
    template_name = 'project/project_create.html'
    model = ProjectTask
    form_class = ProjectTaskForm

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectDelete(DeleteView):
    template_name = 'project/project_delete.html'
    model = ProjectTask
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:project_index')


class ProjectUpdate(UpdateView):
    template_name = "project/project_update.html"
    form_class = ProjectTaskForm
    model = ProjectTask
    context_object_name = 'project'

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})