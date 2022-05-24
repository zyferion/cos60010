from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Available subjects
class Subject(models.Model):
    subject = models.CharField(max_length=100)
    start_dt = models.DateField()
    end_dt = models.DateField()
    
    def __str__(self):
        return str(self.subject) 

# Student enrolments
class Enrolment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE) 
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"user: {self.user}, subject: {self.subject}, is_active: {self.is_active}"
