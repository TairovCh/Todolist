from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import Task, STATUS_CHOICES
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
        return render(request, 'create.html', {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        description = request.POST.get('description')
        if not deadline:
            deadline = None
        new_task = Task.objects.create(title=title, status=status, deadline=deadline, description=description)
        return redirect('task_view', pk=new_task.pk)

def task_update_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_update.html', {'task': task})
    elif request.method == "POST":
        task.title = request.POST.get('title')
        task.status = request.POST.get('status')
        task.deadline = request.POST.get('deadline')
        task.description = request.POST.get('description') 
        task.save()   
        return redirect("task_view", pk=task.pk)   