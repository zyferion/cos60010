from django.urls import path

from . import views

# Define app name
app_name = 'quiz'

# Register views here
urlpatterns = [
    path('', views.index, name='index'),
        
    path('', views.QuizListView.as_view(), name='main-view'),
    path('<pk>/', views.quiz_view, name='quiz-view'),
]