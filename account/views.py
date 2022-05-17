from re import template
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.views import PasswordResetView, LoginView
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html"

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
     template_name = 'account/password_reset_form.html'
     
class AdminLogin(LoginView):
    template_name = 'account/login.html'