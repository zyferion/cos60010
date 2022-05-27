from django.shortcuts import render
from .models import Subject, Enrolment
from django.contrib.auth.decorators import login_required # Import login_required decorator

# Create your views here.
@login_required # Require user logged in before they can access user home page
def home(request):

    user = request.user

    subjects = Subject.objects.all()

    user_enrolments = Enrolment.objects.filter(user=user, is_active=1)

    return render(request, 'subjects/home.html', 
    {   'subjects': subjects, 
        'user_enrolments': user_enrolments
        })

@login_required # Require user logged in before they can access user home page
def subjects(request):

    subjects = Subject.objects.all()
    
    return render(request, 'subjects/subject_list.html', 
    {   'subjects': subjects,
        })
