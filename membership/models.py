from django.db import models


# Create your models here.


class Student(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=70)
    subject=models.CharField(max_length=70)
   