from django.shortcuts import render
from membership.models import Student

# Create your views here.
def membership(request):
    stud = Student.objects.all()
    print("Myoutput",stud)
    return render(request,'membership/membership.html',{'stu': stud})