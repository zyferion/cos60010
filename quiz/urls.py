from django.urls import path

from .views import (
    index,
    QuizListView,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)

# Define app name
app_name = 'quiz'

# Register views here
urlpatterns = [
    path('index/', index, name='index'),

    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', quiz_view, name='quiz-view'),
    path('<pk>/save/', save_quiz_view, name='save-view'),
    path('<pk>/data/', quiz_data_view, name='quiz-data-view'),
]