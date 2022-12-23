from django.shortcuts import reverse
from django.core.paginator import Paginator
from webapp.models import ProjectTask
from webapp.forms import ProjectTaskForm, ProjectUserForm
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

class ProjectIndexView(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'projects'
    model = ProjectTask
    ordering = '-start_date' 


class ProjectView(LoginRequiredMixin, DetailView):
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


class CreateProject(UserPassesTestMixin, CreateView):
    template_name = 'project/project_create.html'
    model = ProjectTask
    form_class = ProjectTaskForm
    context_object_name = 'project'

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.has_perm('webapp.add_projecttask')


    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})




class ProjectDelete(UserPassesTestMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = ProjectTask
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:project_index')

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.has_perm('webapp.delete_projecttask')


class ProjectUpdate(UserPassesTestMixin, UpdateView):
    template_name = "project/project_update.html"
    form_class = ProjectTaskForm
    model = ProjectTask
    context_object_name = 'project'

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.has_perm('webapp.change_projecttask')

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectUserUpdate(UserPassesTestMixin, UpdateView):
    template_name = "project/project_user.html"
    form_class = ProjectUserForm
    model = ProjectTask
    context_object_name = 'project'

    def test_func(self):
        return self.get_object().user == self.request.user or self.request.user.has_perm('webapp.сan_change_user')

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})