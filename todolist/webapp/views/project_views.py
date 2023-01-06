from django.shortcuts import reverse, redirect
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


class CreateProject(PermissionRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    model = ProjectTask
    form_class = ProjectTaskForm
    permission_required = 'webapp.add_projecttask'


    def form_valid(self, form):
        self.object = form.save()
        self.object.user.add(self.request.user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})




class ProjectDelete(PermissionRequiredMixin, DeleteView):
    template_name = 'project/project_delete.html'
    model = ProjectTask
    context_object_name = 'project'
    success_url = reverse_lazy('webapp:project_index')
    permission_required = 'webapp.delete_projecttask'

    def test_func(self):
        return self.get_object().user in self.request.user and self.request.user.has_perm('webapp.delete_projecttask')


class ProjectUpdate(PermissionRequiredMixin, UpdateView):
    template_name = "project/project_update.html"
    form_class = ProjectTaskForm
    model = ProjectTask
    permission_required = 'webapp.change_projecttask'

    def test_func(self):
        return self.get_object().user in self.request.user and self.request.user.has_perm('webapp.change_projecttask')

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})


class ProjectUserUpdate(PermissionRequiredMixin, UpdateView):
    model = ProjectTask
    form_class = ProjectUserForm
    template_name = "project/project_user.html"
    permission_required = 'webapp.сan_add_user'

    def has_permission(self):
        return super().has_permission() and self.request.user in self.get_object().user.all()

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        return reverse('webapp:project_view', kwargs={'pk': self.object.pk})