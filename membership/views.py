from django.shortcuts import render
from membership.models import Student

# Create your views here.
def studentinfo(request):
    stud = Student.objects.all()
    print("Myoutput",stud)
    return render(request,'enroll/studentdetails.html',{'stu': stud})