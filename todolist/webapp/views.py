from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task
from webapp.forms import TaskForm
# Create your views here.


def index_view(request):
    if request.method =="POST":
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('index')

    tasks = Task.objects.all()
    return render(request, 'index.html', {"tasks":tasks})


def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_view.html', {'task': task})



def create_task(request):
    if request.method == "GET":
        form = TaskForm()
        return render(request, 'create.html', { 'form': form })
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = Task.objects.create(
                title = form.cleaned_data["title"],
                status = form.cleaned_data["status"],
                deadline = form.cleaned_data["deadline"],
                description = form.cleaned_data["description"]
            )
            return redirect('task_view', pk=new_task.pk)
        else:
            return render(request, 'create.html', {'form': form})

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        form = TaskForm(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'title':task.title
        })   
        return render(request, 'task_update.html', {'form': form})
    elif request.method == "POST":
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.title = form.cleaned_data.get('title')
            task.status = form.cleaned_data.get('status')
            task.deadline = form.cleaned_data.get('deadline')
            task.description = form.cleaned_data.get('description') 
            task.save()   
            return redirect("task_view", pk=task.pk)   
        else:
            return render(request, "task_update.html", {'form': form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_delete.html', { 'task': task })
    elif request.method == "POST":
        task.delete()
        return redirect('index')