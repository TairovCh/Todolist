from django import forms
from django.forms import widgets
from webapp.models import STATUS_CHOICES

class TaskForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label="Title")
    description = forms.CharField(max_length=3000, required=False, label="Description", widget=widgets.Textarea(attrs={'cols': 20,'rows': 6}))
    status = forms.ChoiceField(choices= STATUS_CHOICES,label='To do status')
    deadline = forms.DateField(required=False, label='To do data')