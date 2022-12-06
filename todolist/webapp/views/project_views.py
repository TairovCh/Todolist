from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.http import urlencode
from django.db.models import Q
from webapp.models import ProjectTask, Task
from webapp.forms import ProjectTaskForm, SimpleSearchForm
from django.views.generic import ListView, CreateView, DetailView


class ProjectIndexView(ListView):
    template_name = 'project/project_index.html'
    context_object_name = 'projects'
    model = ProjectTask
    ordering = ('start_date',)
    

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(Q(name__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class ProjectView(DetailView):
    template_name = 'project/project_view.html'
    model = ProjectTask

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project_task = self.object
        tasks = project_task.tasks.order_by('-create_time')
        context['tasks'] = tasks
        return context


class CreateProject(CreateView):
    template_name = 'project/project_create.html'
    model = ProjectTask
    form_class = ProjectTaskForm

    def get_success_url(self):
        return reverse('project_view', kwargs={'pk': self.project.pk})
    
    def form_valid(self, form):
        self.project = form.save()
        return super().form_valid(form)