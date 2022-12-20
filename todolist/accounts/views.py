from django.shortcuts import redirect
from django.contrib.auth import login
from accounts.forms import MyUserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = MyUserCreationForm
    template_name = 'user_registration.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        next_url = self.request.POST.get('next')
        if next_url:
            return next_url
        return reverse('webapp:index')


