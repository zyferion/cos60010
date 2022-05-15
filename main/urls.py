from django.urls import path

from .views import (
    home
)

app_name = 'main'

# Register views here
urlpatterns = [
    path('home/', home, name='home'),
]
