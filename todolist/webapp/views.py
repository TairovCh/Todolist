from django.shortcuts import render
from webapp.models import Task, STATUS_CHOICES
# Create your views here.


def index_view(request):
    if request.method =="POST":
        task_id = request.GET.get('id')
        task = Task.objects.get(id=task_id)
        task.delete()

    tasks = Task.objects.all()
    return render(request, 'index.html', {"tasks":tasks})

def create_task(request):
    if request.method == "GET":
        return render(request, 'create.html', {'statuses': STATUS_CHOICES})
    elif request.method == "POST":
        title = request.POST.get('title')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')
        if not deadline:
            deadline = None
        new_task = Task.objects.create(title=title, status=status, deadline=deadline)
        return render(request, 'task_view.html', {'task': new_task})