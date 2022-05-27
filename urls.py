from django.urls import path
from django.views.generic.base import RedirectView

from .views import (
    index,
    QuizListView,
    leaderboard,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)

# Define app name
app_name = 'quiz'

# Register views here
urlpatterns = [
    path('index/', index, name='index'),

    path('quiz/', QuizListView.as_view(), name='main-view'),
    path('quiz/<pk>/', quiz_view, name='quiz-view'),
    path('quiz/<pk>/save/', save_quiz_view, name='save-view'),
    path('quiz/<pk>/data/', quiz_data_view, name='quiz-data-view'),
    path('leaderboard/', leaderboard, name = 'leaderboard')
]