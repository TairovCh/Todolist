from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils.http import urlencode
from django.db.models import Q
from webapp.models import Task
from webapp.forms import TaskForm, SimpleSearchForm
from django.views.generic import TemplateView, View, FormView, ListView, UpdateView


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


class CreateTask(FormView):
    template_name = 'tasks/create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})
    
    def form_valid(self, form):
        self.task = form.save()
        return super().form_valid(form)


class UpdateTask(UpdateView):

    template_name = "tasks/task_update.html"
    form_class = TaskForm
    model = Task
    context_object_name = 'task'

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.object.pk})


class DeleteTask(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'tasks/task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')



