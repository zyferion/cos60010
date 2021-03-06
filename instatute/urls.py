"""instatute URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from users import views as user_views
from django.contrib.auth import views as auth_views
from subjects import views as subjects_views
from membership import views as membership_views
from quiz import views as quiz_views

urlpatterns = [
    # Main homepage
    # FIXME: this should be a public homepage not a redirect to the Dashboard
    path('', lambda req: redirect('/home/')),

    # Admin
    path('admin/', admin.site.urls),

    # Quiz App
    path('', include('quiz.urls', namespace='quiz')),
    path('leaderboard/', quiz_views.leaderboard, name='leaderboard'),

    # Users App
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),

    # Subjects App
    path('home/', subjects_views.home, name='home'),
    path('classes/', subjects_views.subjects, name='classes'),

    # Membership App
    path('membership/', membership_views.membership, name='membership')
]

# Add static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Customise Django Admin interface
admin.site.site_header = 'Instatute'
admin.site.index_title = 'Staff Admin Area'
admin.site.site_title = 'Instatute Staff Admin Area'