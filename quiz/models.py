from django.db import models
from django.contrib.auth.models import User
import random

# Create your models here.

# Quiz model
class Quiz(models.Model):
    name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)
    number_of_questions = models.IntegerField()
    active_status = models.BooleanField(default=False)
    start_dttm = models.DateTimeField()
    end_dttm = models.DateTimeField()

    # define function
    def __str__(self):
        return f"{self.name}--{self.subject}"
    
    # randomize questions
    def get_questions(self):
        questions = list(self.question_set.all()) # store all questions in a list
        random.shuffle(questions) # shuffle order
        return questions[:self.number_of_questions]
    
    # define plural
    class Meta:
        verbose_name_plural = 'Quizes'


# Question model
class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE) # Foreign key = Quiz
    created_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


# Answer model
class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_dttm = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

# Results
class Result(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk) 


