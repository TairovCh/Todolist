from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError

class MyUserCreationForm(UserCreationForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if email == '':
            self.add_error('email', ValidationError('Почта обязательно к заполнению', code='error_email'))
        return email


    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        if first_name == '':
            if last_name == '':
                raise forms.ValidationError('Заполните Имя или Фамилию!', code='error_first_last_name')

    class Meta(UserCreationForm.Meta):
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']









#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password_confirm = cleaned_data.get("password_confirm")
#         if password != password_confirm:
#             raise forms.ValidationError('Пароли не совпадают!')
#         return cleaned_data


