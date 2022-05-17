#from atexit import register
#from urllib.parse import urlparse
#from unicodedata import name
from django.urls import path
from .views import SignUpView
from .views import ResetPasswordView
from .views import AdminLogin

app_name = "account"

urlpatterns = [
   # path("", views.homepage, name="homepage"),
    path("signup/", SignUpView.as_view(), name="register"),
    path("password_reset_form/", ResetPasswordView.as_view(), name="resetpassword"),
    path("login/", AdminLogin.as_view(), name="login")
    #path("logout/", views.logout_request, name="logout"),
]