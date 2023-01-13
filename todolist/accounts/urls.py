from django.urls import path
from accounts.views import RegisterView, UserDetailView, UsersView, UserChangeView, UserPasswordChangeView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'


urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path('<int:pk>/', UserDetailView.as_view(), name='detail'),
    path('users/', UsersView.as_view(), name='users_list'),
    path('change/',  UserChangeView.as_view(), name='change'),
    path('password_change/', UserPasswordChangeView.as_view(), name='password_change'),
]