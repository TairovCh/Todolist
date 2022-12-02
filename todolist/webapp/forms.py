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
        bans = ['test_1', 'test_2', "test_3"]
        if len(summary) < 5:
            self.add_error('summary', ValidationError('Длина поля должна составлять не меенее %(length)d символов!', code='too_short', params={'length': 5}))
        elif len(summary) > 50:
            self.add_error('summary', ValidationError('Длина поля должна составлять не более %(length)d символов!', code='too_long', params={'length': 50}))
        for ban in bans:
            if summary == ban:
                self.add_error('summary', ValidationError("Эти слова запрешено вводить!"))
        return summary


    def clean_description(self):
        description = self.cleaned_data['description']
        bans = ['test_1', 'test_2', "test_3"]
        for ban in bans:
            for desc in description.split():
                if desc == ban:
                    self.add_error('summary', ValidationError("Эти слова запрешено вводить!"))
        if len(description) < 30:
            self.add_error('description', ValidationError('Длина поля должна составлять не меенее %(length)d символов!', code='too_short', params={'length': 30}))
        return description

