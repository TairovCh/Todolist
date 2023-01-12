from django.shortcuts import redirect
from django.contrib.auth import login
from accounts.forms import MyUserCreationForm
from django.views.generic import CreateView, DetailView, ListView
from django.urls import reverse
from accounts.models import Profile
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.list import MultipleObjectMixin

# Create your views here.

class RegisterView(CreateView):
    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'user_registration.html'

    def form_valid(self, form):
        user = form.save()
        Profile.objects.create(user=user)
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


class UserDetailView(LoginRequiredMixin, DetailView, MultipleObjectMixin):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        projects = self.get_object().projecttasks.all()
        return super().get_context_data(object_list=projects, **kwargs)



class UsersView(PermissionRequiredMixin, ListView):
    template_name = 'users.html'
    context_object_name = 'users_list'
    model = get_user_model() 
    paginate_by = 3
    permission_required = 'accounts.view_profile'

