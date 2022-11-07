from django.shortcuts import render
from webapp.models import Task
# Create your views here.


def index_view(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {"tasks":tasks})