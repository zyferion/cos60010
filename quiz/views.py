from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView
from django.http import HttpResponse

from .models import Quiz

# Create your views here.# Create your views here.

def index(request):
    return HttpResponse("Hello world!")

class QuizListView(ListView):
    model = Quiz
    template = 'quiz/main.html'

def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz/quiz.html', {'obj': quiz})