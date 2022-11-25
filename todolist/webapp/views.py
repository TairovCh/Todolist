from django.shortcuts import render, get_object_or_404, redirect, reverse
from webapp.models import Task
from webapp.forms import TaskForm
from django.views.generic import TemplateView, View, FormView
# Create your views here.




class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.all()
        return context


class TaskView(TemplateView):
    template_name = 'task_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["task"] = get_object_or_404(Task, pk=kwargs['pk'])
        return context
        


class CreateTask(FormView):
    template_name = 'create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})
    
    def form_valid(self, form):
        self.task = form.save()
        # type_task = form.cleaned_data.pop('type_task')
        # self.task = Task.objects.create(**form.cleaned_data)
        # self.task.type_task.set(type_task)
        return super().form_valid(form)


class UpdateTask(FormView):

    template_name = "task_update.html"
    form_class = TaskForm

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Task, pk=pk)

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = self.task
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs



    # def get_initial(self):
    #     initial = {}
    #     for key in 'summary', 'description', 'status':
    #         initial[key] = getattr(self.task, key)
    #     initial['type_task'] = self.task.type_task.all()
    #     return initial

    def form_valid(self, form):
        # type_task = form.cleaned_data.pop('type_task')
        # for key, value in form.cleaned_data.items():
        #     if value is not None:
        #         setattr(self.task, key, value)
        # self.task.save()
        # self.task.type_task.set(type_task)
        self.task = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('task_view', kwargs={'pk': self.task.pk})





class DeleteTask(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.delete()
        return redirect('index')



