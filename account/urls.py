#from atexit import register
#from urllib.parse import urlparse
from unicodedata import name
from django.urls import path
from . import views

app_name = "account"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
]