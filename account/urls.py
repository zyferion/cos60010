
from django.urls import path
from .views import SignUpView
from .views import ResetPasswordView
from .views import AdminLogin

app_name = "account"

urlpatterns = [

    path("signup/", SignUpView.as_view(), name="register"),
    path("password_reset_form/", ResetPasswordView.as_view(), name="resetpassword"),
    path("login/", AdminLogin.as_view(), name="login")

]