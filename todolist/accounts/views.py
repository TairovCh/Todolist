from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from accounts.forms import MyUserCreationForm

# Create your views here.
def register_view(request, *args, **kwargs):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('webapp:index')
    return render(request, 'user_registration.html', {'form': form})


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:index')