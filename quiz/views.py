from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from .models import Quiz
from django.http import JsonResponse

# Create your views here.

# index
def index(request):
    template = loader.get_template('quiz/index.html')
    return HttpResponse(template.render())

# main
class QuizListView(ListView):
    model = Quiz
    template = 'quiz/main.html' #for some reason this looks for quiz_list.html

# quiz
def quiz_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)
    return render(request, 'quiz/quiz.html', {'obj': quiz})

# quiz data
def quiz_data_view(request, pk):
    quiz = Quiz.objects.get(pk=pk)  

    # get the quiz questions
    # initialise as empty list
    questions = [] 
    for q in quiz.get_questions():
        # create empty answers list
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q):answers}) #create a dictionary with question-answer key-value pairs
    
    return JsonResponse({
        'data': questions
    })

# save quiz attempt
def save_quiz_view(request, pk):
    print(request.POST)
    return JsonResponse({'text':'works'})