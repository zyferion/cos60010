from django.shortcuts import render
from .models import Subject, Enrolment
from django.contrib.auth.decorators import login_required # Import login_required decorator
from quiz.models import Quiz, Result
from django.db.models import Avg

# Create your views here.
@login_required # Require user logged in before they can access user home page
def home(request):

    user = request.user

    subjects = Subject.objects.all()

    quizzes = Quiz.objects.all()

    user_enrolments = Enrolment.objects.filter(user=user, is_active=1)
    user_results = Result.objects.filter(user=user)

    # count of user quiz attempts
    quiz_count = user_results.count()

    # count of user enrolments
    enrolments_count = user_enrolments.count()

    # average result score
    avg_score = user_results.aggregate(Avg('score')).get('score__avg')
    avg_score = round(avg_score,2)

    return render(request, 'subjects/home.html', 
    {   'subjects': subjects, 
        'user_enrolments': user_enrolments,
        'user_results': user_results,
        'quiz_count' : quiz_count,
        'enrolments_count' : enrolments_count,
        'avg_score': avg_score,
        'quizzes': quizzes,
        })

@login_required # Require user logged in before they can access user home page
def subjects(request):

    subjects = Subject.objects.all()
    
    return render(request, 'subjects/subject_list.html', 
    {   'subjects': subjects,
        })