from pickle import TRUE
from unittest import result
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView
from django.http import HttpResponse
from django.template import loader
from .models import Question, Quiz, Answer, Result
from django.http import JsonResponse
from django.db import models
from django.contrib.auth.decorators import login_required # Import login_required decorator
from subjects.models import Enrolment
from django.db.models import Avg, F
#from datetime import datetime

# Create your views here.

# index
def index(request):
    #template = loader.get_template('quiz/index.html')
    #return HttpResponse(template.render())
    return render(request, 'quiz/index.html')
    
# main quiz list
class QuizListView(ListView):
    model = Quiz
    template = 'quiz/quiz_list.html'

# quiz
@login_required # Require user logged in before they can access
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

# def is_ajax function (since it is deprecated)
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


# save quiz attempt
def save_quiz_view(request, pk):
    #print(request.POST)

    if is_ajax(request=request):
        # initialise empty questions list
        questions = []
        data = request.POST
        data_ = dict(data.lists())

        data_.pop('csrfmiddlewaretoken') #remove the csrf token from the data dictionary

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k) #get question by the key
            questions.append(question)
        print(questions)

        user = request.user
        quiz = Quiz.objects.get(pk=pk)
        subject = quiz.subject
        number_of_questions = quiz.number_of_questions
        score = 0
        multiplier = 100 / number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            # grab the user selected answer
            a_selected = request.POST.get(q.text)
            #print('selected ', a_selected)

            # grab the correct answer
            correct_answer = Answer.objects.get(question=q,correct=True)
            correct_answer = correct_answer.text

            # check if answer was selected (not empty)
            # if yes check if it is correct
            if a_selected != "":
                if a_selected == correct_answer:
                    score += 1
                    results.append({str(q): {'answered': a_selected, 'correct_answer': correct_answer}})
                else:
                    results.append({str(q): {'answered': a_selected, 'correct_answer': correct_answer}})
            else: # no need to store correct answer if unattempted
                #print('unattempted!')
                results.append({str(q): {'answered': 'not answered'}})

        score_ = score * multiplier
        score_ = round(score_,2)
        Result.objects.create( user=user, subject=subject, quiz=quiz, score=score_, created_dttm=models.DateTimeField(auto_now=True))
 
    return JsonResponse({'score':score, 'score_':score_, 'results': results, 'num_questions': number_of_questions})


# leaderboard

def leaderboard(request):

    leaderboard1 = Result.objects.filter(subject = 'MATH101').values('user','subject').annotate(avg_score=Avg('score')).order_by('-avg_score')[0:10]
    leaderboard2 = Result.objects.filter(subject = 'PHYSICS101').values('user','subject').annotate(avg_score=Avg('score')).order_by('-avg_score')[0:10]
    leaderboard3 = Result.objects.filter(subject = 'BIOLOGY101').values('user','subject').annotate(avg_score=Avg('score')).order_by('-avg_score')[0:10]

    context = {
        'leaderboard1' : leaderboard1,
        'leaderboard2' : leaderboard2,
        'leaderboard3' : leaderboard3,
    }
    return render(request, 'quiz/leaderboard.html', context)
   




