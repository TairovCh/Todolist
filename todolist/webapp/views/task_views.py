from django.shortcuts import get_object_or_404, reverse
from django.urls import reverse_lazy
from django.utils.http import urlencode
from django.db.models import Q
from webapp.models import Task
from webapp.forms import TaskForm, SimpleSearchForm
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(ListView):
    template_name = 'tasks/index.html'
    context_object_name = 'tasks'
    model = Task
    ordering = ('create_time', 'update_time',)
    paginate_by = 10
    

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
            queryset = queryset.filter(Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
            context['search'] = self.search_value
        return context


class TaskView(TemplateView):
    template_name = 'tasks/task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=kwargs['pk'])
        return context


class CreateTask(LoginRequiredMixin, CreateView):
    template_name = 'tasks/create.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})


class UpdateTask(UpdateView):

    template_name = "tasks/task_update.html"
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('webapp:task_view', kwargs={'pk': self.object.pk})


class DeleteTask(DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('webapp:index')