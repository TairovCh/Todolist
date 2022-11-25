from django import forms
from django.forms import widgets, ValidationError
from webapp.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['summary', 'description', 'status', 'type_task']
        widgets = {'type_task': widgets.CheckboxSelectMultiple}




    def clean_summary(self):
        summary = self.cleaned_data['summary']
        if len(summary) < 5:
            self.add_error('summary', ValidationError('Длина поля должна составлять не меенее %(length)d символов!', code='too_short', params={'length': 5}))
        elif len(summary) > 50:
            self.add_error('summary', ValidationError('Длина поля должна составлять не более %(length)d символов!', code='too_long', params={'length': 50}))
        return summary

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 30:
            self.add_error('description', ValidationError('Длина поля должна составлять не меенее %(length)d символов!', code='too_short', params={'length': 30}))
        return description


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['summary'] == cleaned_data.get('description', ''):
            raise ValidationError('Краткое описание и полное описание не должны быть одинаковыми')
        return cleaned_data