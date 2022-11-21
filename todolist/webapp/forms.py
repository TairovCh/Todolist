from django import forms
from django.forms import widgets
from webapp.models import StatusTask, TypeTask

class TaskForm(forms.Form):
    summary = forms.CharField(max_length=60, required=True, label='Краткое описание')
    description = forms.CharField(max_length=3000, required=False, widget=widgets.Textarea, label="Полное описание")
    status = forms.ModelChoiceField(queryset=StatusTask.objects.all(), required=True, label='Статус')
    type_task = forms.ModelChoiceField(queryset=TypeTask.objects.all(), required=True, label='Тип')
